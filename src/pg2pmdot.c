#define _POSIX_C_SOURCE 200809L

#include <errno.h>
#include <getopt.h>
#include <inttypes.h>
#include <limits.h>
#include <stdlib.h>
#include <string.h>

#include "cli_version.h"
#include "json_utils.h"
#include "pg_preprocess.h"
#include "pm_tree_dot.h"
#include "strahler_tree_version.h"

enum { EXIT_GAME = 3, EXIT_SOLVER = 4, EXIT_IO = 5 };

typedef struct {
  PGGame const *game;
  PGPreprocessResult const *preprocessed;
  ADDotPlayer player;
  ADDotLabels labels;
  size_t max_items;
  bool original;
  bool leaves;
  bool json;
  bool wrote_round;
  bool stats;
  bool incremental;
  char const *start_winner;
} Output;

static void usage(FILE *out, char *argv[]) {
  cli_usage(out, argv[0], " [FILE]");
  fputs("  --algorithm=strahler|succinct               default: strahler\n"
        "  --format=dot|leaves|json                    default: dot\n"
        "  --player=both|even|odd                      default: both\n"
        "  --labels=counts|sets|none                   default: counts\n"
        "  --max-set-items=N                           default: 32\n"
        "  --priority-mode=original|compact            default: original\n"
        "  --initial-shave=single,loops,wcwc|all|none  default: none\n"
        "  --compress                                  Merge same-parity "
        "priorities (default: off)\n"
        "  --k=K                                       Fixed Strahler "
        "parameter; requires --t\n"
        "  --t=T                                       Fixed leaf-budget "
        "exponent; requires --k\n"
        "  --bits=B                                    Fixed succinct bit "
        "budget; may be partial\n"
        "  --iter-shave                                Remove dominions "
        "between runs (default: off)\n"
        "  --stats                                     Print statistics to "
        "stderr (default: off)\n"
        "  --no-verify                                 Skip verification "
        "(default: verify)\n"
        "Default parameters guarantee a complete result. FILE defaults to "
        "stdin; - reads stdin.\n",
        out);
}

static bool parse_size(char const *text, size_t *value) {
  if (text == nullptr || text[0] == '\0' ||
      strspn(text, "0123456789") != strlen(text)) {
    return false;
  }
  errno = 0;
  char *end = nullptr;
  uintmax_t const parsed = strtoumax(text, &end, 10);
  if (errno == ERANGE || *end != '\0' || parsed > INT_MAX) {
    return false;
  }
  *value = (size_t)parsed;
  return true;
}

static bool write_output(PMResult const result[static 2],
                         PGSet const *unresolved, size_t const round,
                         void *context) {
  Output *output = context;
  bool const partial = !pg_set_empty(unresolved);
  if (output->stats) {
    if (output->incremental) {
      fprintf(stderr, "iter-shave: rounds=%zu shaved=%zu\n", round,
              pg_set_count(&result[0].region) +
                  pg_set_count(&result[1].region) +
                  pg_set_count(&result[0].attracted) +
                  pg_set_count(&result[1].attracted));
    }
    fprintf(stderr, "%s: round=%zu result=%s unresolved=%zu\n",
            result[0].algorithm == PM_STRAHLER ? "strahler" : "succinct", round,
            partial ? "partial" : "complete", pg_set_count(unresolved));
    for (size_t player = 0; player < 2; player++) {
      PMResult const *current = &result[player];
      size_t const start = output->game->start_vertex;
      if (pg_set_contains(&output->preprocessed->won[player], start) ||
          pg_set_contains(&current->region, start) ||
          pg_set_contains(&current->attracted, start)) {
        output->start_winner = player == PG_EVEN ? "even" : "odd";
      }
      fprintf(stderr, "%s: ", player == PG_EVEN ? "even" : "odd");
      if (current->algorithm == PM_STRAHLER) {
        fprintf(stderr, "k=%zu t=%zu ", current->parameters.k,
                current->parameters.t);
      } else {
        fprintf(stderr, "bits=%zu ", current->parameters.bits);
      }
      fprintf(stderr,
              "depth=%d vertices=%zu lifts=%zu attempts=%zu non_top=%zu "
              "top=%zu attracted=%zu\n",
              current->depth, current->active_count, current->lifts,
              current->attempts, pg_set_count(&current->region),
              current->active_count - pg_set_count(&current->region),
              pg_set_count(&current->attracted));
    }
  }
  if (output->json) {
    if (output->wrote_round) {
      fputc(',', stdout);
    }
    output->wrote_round = true;
    return pm_write_json(
        stdout, output->game, result, unresolved, round, output->player,
        output->original ? &output->preprocessed->priority_map : nullptr,
        output->preprocessed->won);
  }
  if (output->leaves) {
    if (output->incremental) {
      if (result[0].algorithm == PM_STRAHLER) {
        if (fprintf(stdout, "# round %zu k=%zu t=%zu\n", round,
                    result[0].parameters.k, result[0].parameters.t) < 0) {
          return false;
        }
      } else if (fprintf(stdout, "# round %zu bits=%zu\n", round,
                         result[0].parameters.bits) < 0) {
        return false;
      }
    }
    for (size_t player = 0; player < 2; player++) {
      if ((output->player == AD_DOT_PLAYER_EVEN && player != PG_EVEN) ||
          (output->player == AD_DOT_PLAYER_ODD && player != PG_ODD)) {
        continue;
      }
      if (fputs(player == PG_EVEN ? "even: " : "odd: ", stdout) < 0 ||
          !pm_write_leaves(stdout, &result[player])) {
        return false;
      }
    }
    return true;
  }
  return pm_write_dot(
      stdout, output->game, result, unresolved, round, output->incremental,
      output->player, output->labels, output->max_items,
      output->original ? &output->preprocessed->priority_map : nullptr,
      output->preprocessed->won);
}

int main(int argc, char *argv[argc + 1]) {
  enum {
    OPT_ALGORITHM = 256,
    OPT_FORMAT,
    OPT_PLAYER,
    OPT_LABELS,
    OPT_MAX_ITEMS,
    OPT_PRIORITY,
    OPT_SHAVE,
    OPT_COMPRESS,
    OPT_K,
    OPT_T,
    OPT_BITS,
    OPT_INCREMENTAL,
    OPT_STATS,
    OPT_NO_VERIFY
  };
  static struct option const options[] = {
      {"help", no_argument, nullptr, 'h'},
      {"version", no_argument, nullptr, 'v'},
      {"algorithm", required_argument, nullptr, OPT_ALGORITHM},
      {"format", required_argument, nullptr, OPT_FORMAT},
      {"player", required_argument, nullptr, OPT_PLAYER},
      {"labels", required_argument, nullptr, OPT_LABELS},
      {"max-set-items", required_argument, nullptr, OPT_MAX_ITEMS},
      {"priority-mode", required_argument, nullptr, OPT_PRIORITY},
      {"initial-shave", required_argument, nullptr, OPT_SHAVE},
      {"compress", no_argument, nullptr, OPT_COMPRESS},
      {"k", required_argument, nullptr, OPT_K},
      {"t", required_argument, nullptr, OPT_T},
      {"bits", required_argument, nullptr, OPT_BITS},
      {"iter-shave", no_argument, nullptr, OPT_INCREMENTAL},
      {"stats", no_argument, nullptr, OPT_STATS},
      {"no-verify", no_argument, nullptr, OPT_NO_VERIFY},
      {nullptr, 0, nullptr, 0},
  };
  PMOptions solve_options = {.algorithm = PM_STRAHLER, .verify = true};
  PGPreprocessOptions preprocess_options = {0};
  Output output = {.player = AD_DOT_PLAYER_BOTH,
                   .labels = AD_DOT_LABEL_COUNTS,
                   .max_items = 32,
                   .original = true,
                   .start_winner = "unresolved"};
  bool k_given = false;
  bool t_given = false;
  bool bits_given = false;
  int option = 0;
  while ((option = cli_getopt(argc, argv, options)) != -1) {
    switch (option) {
    case 'v':
      return cli_print_version(argv[0]);
    case 'h':
      usage(stdout, argv);
      return EXIT_SUCCESS;
    case OPT_ALGORITHM:
      if (strcmp(optarg, "strahler") == 0) {
        solve_options.algorithm = PM_STRAHLER;
      } else if (strcmp(optarg, "succinct") == 0) {
        solve_options.algorithm = PM_SUCCINCT;
      } else {
        goto invalid;
      }
      break;
    case OPT_FORMAT:
      output.json = false;
      if (strcmp(optarg, "dot") == 0) {
        output.leaves = false;
      } else if (strcmp(optarg, "json") == 0) {
        output.json = true;
        output.leaves = false;
      } else if (strcmp(optarg, "leaves") == 0) {
        output.leaves = true;
      } else {
        goto invalid;
      }
      break;
    case OPT_PLAYER:
      if (strcmp(optarg, "both") == 0) {
        output.player = AD_DOT_PLAYER_BOTH;
      } else if (strcmp(optarg, "even") == 0) {
        output.player = AD_DOT_PLAYER_EVEN;
      } else if (strcmp(optarg, "odd") == 0) {
        output.player = AD_DOT_PLAYER_ODD;
      } else {
        goto invalid;
      }
      break;
    case OPT_LABELS:
      if (strcmp(optarg, "counts") == 0) {
        output.labels = AD_DOT_LABEL_COUNTS;
      } else if (strcmp(optarg, "sets") == 0) {
        output.labels = AD_DOT_LABEL_SETS;
      } else if (strcmp(optarg, "none") == 0) {
        output.labels = AD_DOT_LABEL_NONE;
      } else {
        goto invalid;
      }
      break;
    case OPT_MAX_ITEMS:
      if (!parse_size(optarg, &output.max_items)) {
        goto invalid;
      }
      break;
    case OPT_PRIORITY:
      if (strcmp(optarg, "original") == 0) {
        output.original = true;
      } else if (strcmp(optarg, "compact") == 0) {
        output.original = false;
      } else {
        goto invalid;
      }
      break;
    case OPT_SHAVE:
    case OPT_COMPRESS:
      if (!pg_preprocess_parse_option(
              &preprocess_options,
              option == OPT_SHAVE ? "initial-shave" : "compress", optarg)) {
        goto invalid;
      }
      break;
    case OPT_K:
      k_given = true;
      if (!parse_size(optarg, &solve_options.parameters.k) ||
          solve_options.parameters.k == 0) {
        goto invalid;
      }
      break;
    case OPT_T:
      t_given = true;
      if (!parse_size(optarg, &solve_options.parameters.t)) {
        goto invalid;
      }
      break;
    case OPT_BITS:
      bits_given = true;
      if (!parse_size(optarg, &solve_options.parameters.bits)) {
        goto invalid;
      }
      break;
    case OPT_INCREMENTAL:
      solve_options.incremental = true;
      output.incremental = true;
      break;
    case OPT_STATS:
      output.stats = true;
      break;
    case OPT_NO_VERIFY:
      solve_options.verify = false;
      break;
    default:
      goto invalid;
    }
  }
  if (argc - optind > 1 || k_given != t_given ||
      (solve_options.algorithm == PM_STRAHLER && bits_given) ||
      (solve_options.algorithm == PM_SUCCINCT && (k_given || t_given))) {
    goto invalid;
  }
  solve_options.fixed = k_given || bits_given;
  FILE *input = stdin;
  if (optind < argc && strcmp(argv[optind], "-") != 0) {
    input = fopen(argv[optind], "rb");
    if (input == nullptr) {
      fprintf(stderr, "Cannot open %s: %s\n", argv[optind], strerror(errno));
      return EXIT_IO;
    }
  }
  PGGame game = {0};
  PGParseError parse_error = {0};
  bool const parsed = pg_game_read(input, &game, &parse_error);
  bool const closed = input == stdin || fclose(input) == 0;
  if (!parsed || !closed) {
    if (!parsed) {
      fprintf(stderr, "%zu:%zu: %s\n", parse_error.line, parse_error.column,
              parse_error.message);
    } else {
      fputs("Failed to close input\n", stderr);
    }
    pg_game_destroy(&game);
    return parsed ? EXIT_IO : EXIT_GAME;
  }
  int status = EXIT_SOLVER;
  PGPreprocessResult preprocessed = {0};
  errno = 0;
  if (!pg_preprocess(&game, &preprocess_options, &preprocessed) ||
      (solve_options.verify && !pg_preprocess_verify(&game, &preprocessed))) {
    fputs("Failed to preprocess or verify shaved regions\n", stderr);
    goto cleanup;
  }
  output.game = &game;
  output.preprocessed = &preprocessed;
  if (output.stats &&
      (preprocess_options.shave != 0 || preprocess_options.compress)) {
    fprintf(stderr,
            "preprocess: residual=%zu shaved_even=%zu shaved_odd=%zu "
            "single=%zu loops=%zu wcwc=%zu\n",
            pg_set_count(&preprocessed.active),
            pg_set_count(&preprocessed.won[0]),
            pg_set_count(&preprocessed.won[1]),
            preprocessed.shaved[PG_SHAVE_SINGLE][0] +
                preprocessed.shaved[PG_SHAVE_SINGLE][1],
            preprocessed.shaved[PG_SHAVE_LOOPS][0] +
                preprocessed.shaved[PG_SHAVE_LOOPS][1],
            preprocessed.shaved[PG_SHAVE_WCWC][0] +
                preprocessed.shaved[PG_SHAVE_WCWC][1]);
  }
  if (output.json) {
    fputc('{', stdout);
    json_header(stdout, "strahler-pm/1",
                STRAHLER_TREE_VERSION " (git " STRAHLER_TREE_GIT ")",
                solve_options.algorithm == PM_STRAHLER ? "strahler"
                                                       : "succinct",
                argc, argv);
    fputs(",\"game\":", stdout);
    json_game(stdout, &game, &preprocessed.priority_map);
    fputs(",\"rounds\":[", stdout);
  }
  PMError error = {0};
  if (!pm_solve(&game, &preprocessed.active, &solve_options, write_output,
                &output, &error)) {
    fprintf(stderr, "Solver failed: %s\n", error.message);
    goto cleanup;
  }
  if (output.json) {
    fputs("]}\n", stdout);
  }
  if (output.stats) {
    fprintf(stderr, "start: vertex=%" PRIu64 " winner=%s\n", game.start_id,
            output.start_winner);
  }
  status = fflush(stdout) == 0 && fflush(stderr) == 0 && !ferror(stdout) &&
                   !ferror(stderr)
               ? EXIT_SUCCESS
               : EXIT_IO;
cleanup:
  // Boolean solver/output APIs propagate allocation failure through errno.
  if (status != EXIT_SUCCESS && errno == ENOMEM) {
    fputs("Failed to allocate memory\n", stderr);
  }
  pg_preprocess_destroy(&preprocessed);
  pg_game_destroy(&game);
  return status;
invalid:
  return cli_error(argv[0], "Invalid or incompatible option; use --name=value "
                            "(Strahler requires both --k and --t)");
}
