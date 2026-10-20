#define _POSIX_C_SOURCE 200809L

#include <getopt.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cli_version.h"
#include "pg_game.h"

typedef enum {
  PRIORITY_MODE_ORIGINAL,
  PRIORITY_MODE_COMPACT,
} PriorityMode;

static void print_usage(FILE *out, char *argv[]) {
  cli_usage(out, argv[0], "");
  fputs("  --normalize                                 Write canonical "
        "PGSolver format (default: summary)\n"
        "  --priority-mode=original|compact            Choose output "
        "priorities (default: original)\n"
        "Read one PGSolver game from standard input.\n",
        out);
}

int main(int argc, char *argv[argc + 1]) {
  static struct option const options[] = {
      {"help", no_argument, nullptr, 'h'},
      {"version", no_argument, nullptr, 'v'},
      {"normalize", no_argument, nullptr, 'n'},
      {"priority-mode", required_argument, nullptr, 1},
      {nullptr, 0, nullptr, 0},
  };

  bool normalize = false;
  PriorityMode priority_mode = PRIORITY_MODE_ORIGINAL;
  int option = 0;
  while ((option = cli_getopt(argc, argv, options)) != -1) {
    switch (option) {
    case 'v':
      return cli_print_version(argv[0]);
    case 'h':
      print_usage(stdout, argv);
      return EXIT_SUCCESS;
    case 'n':
      normalize = true;
      break;
    case 1:
      if (strcmp(optarg, "original") == 0) {
        priority_mode = PRIORITY_MODE_ORIGINAL;
      } else if (strcmp(optarg, "compact") == 0) {
        priority_mode = PRIORITY_MODE_COMPACT;
      } else {
        return cli_error(argv[0], "Invalid --priority-mode value");
      }
      break;
    default:
      return cli_error(argv[0],
                       "Unknown option or invalid argument; use --name=value");
    }
  }
  if (optind != argc) {
    return cli_error(argv[0],
                     "Unknown option or invalid argument; use --name=value");
  }

  PGGame game = {0};
  PGParseError error = {0};
  if (!pg_game_read(stdin, &game, &error)) {
    fprintf(stderr, "%zu:%zu: %s\n", error.line, error.column, error.message);
    return EXIT_FAILURE;
  }

  PGPriorityMap priority_map = {0};
  bool compacted = false;
  if (priority_mode == PRIORITY_MODE_COMPACT) {
    if (!pg_priority_map_build(&game, &priority_map) ||
        !pg_priority_map_apply(&priority_map, &game)) {
      pg_priority_map_destroy(&priority_map);
      pg_game_destroy(&game);
      fputs("Failed to compact the game priorities\n", stderr);
      return EXIT_FAILURE;
    }
    compacted = true;
  }

  bool succeeded = true;
  if (normalize) {
    succeeded = pg_game_write_pgsolver(stdout, &game, true);
  } else {
    size_t owners[2] = {0};
    for (size_t index = 0; index < game.vertex_count; index++) {
      owners[game.vertices[index].owner]++;
    }
    uint64_t const minimum_id = game.vertices[0].external_id;
    uint64_t const maximum_id =
        game.vertices[game.vertex_count - 1].external_id;
    succeeded =
        printf("vertices: %zu\n", game.vertex_count) >= 0 &&
        printf("edges: %zu\n", game.edge_count) >= 0 &&
        printf("max-priority: %" PRIu64 "\n", game.max_priority) >= 0 &&
        printf("owners: %zu %zu\n", owners[PG_EVEN], owners[PG_ODD]) >= 0 &&
        printf("external-id-range: %" PRIu64 "..%" PRIu64 "\n", minimum_id,
               maximum_id) >= 0;
  }
  bool const restored =
      !compacted || pg_priority_map_restore(&priority_map, &game);
  pg_priority_map_destroy(&priority_map);
  pg_game_destroy(&game);
  if (!succeeded) {
    fputs("Failed to write output\n", stderr);
    return EXIT_FAILURE;
  }
  if (!restored) {
    fputs("Failed to restore the source priorities\n", stderr);
    return EXIT_FAILURE;
  }
  return EXIT_SUCCESS;
}
