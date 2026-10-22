// We will be using getopt, and it is NOT part of the C standard, so we
// use the feature test macro for the 2008 edition of the POSIX standard

#define _POSIX_C_SOURCE 200809L

#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cli_version.h"
#include "json_utils.h"
#include "ordered_tree.h"
#include "strahler_tree_version.h"

enum { OPT_CHECK_ORDER = 256, OPT_REORDER, OPT_FORMAT };

static void print_usage(FILE *out, char *argv[]) {
  cli_usage(out, argv[0], "");
  fputs("  --format=dot|json                           default: dot\n"
        "  --check-order                               Reject branches outside "
        "bitstring-vector order\n"
        "  --reorder                                   Sort branches into "
        "bitstring-vector order\n"
        "Read progress measures ending with | from standard input.\nEach "
        "measure is a comma-separated vector of bitstrings.\nDefault: preserve "
        "input order. --check-order and --reorder are exclusive.\nBitstrings "
        "use infinite-binary-tree DFS order (0 beta < e < 1 beta);\nvectors "
        "are compared lexicographically.\n",
        out);
}

int main(int argc, char *argv[argc + 1]) {
  int opt;
  bool json = false;
  OrderedTreeBranchOrder branch_order = ORDERED_TREE_PRESERVE_INPUT_ORDER;
  static struct option const long_options[] = {
      {"help", no_argument, nullptr, 'h'},
      {"version", no_argument, nullptr, 'v'},
      {"format", required_argument, nullptr, OPT_FORMAT},
      {"check-order", no_argument, nullptr, OPT_CHECK_ORDER},
      {"reorder", no_argument, nullptr, OPT_REORDER},
      {nullptr, 0, nullptr, 0},
  };

  while ((opt = cli_getopt(argc, argv, long_options)) != -1) {
    switch (opt) {
    case 'v':
      return cli_print_version(argv[0]);
    case 'h':
      print_usage(stdout, argv);
      return EXIT_SUCCESS;
    case OPT_FORMAT:
      if (strcmp(optarg, "json") == 0) {
        json = true;
      } else if (strcmp(optarg, "dot") == 0) {
        json = false;
      } else {
        return cli_error(argv[0], "Invalid --format value");
      }
      break;
    case OPT_CHECK_ORDER:
      if (branch_order == ORDERED_TREE_REORDER_VECTOR_ORDER) {
        return cli_error(argv[0],
                         "--check-order and --reorder are mutually exclusive");
      }
      branch_order = ORDERED_TREE_CHECK_VECTOR_ORDER;
      break;
    case OPT_REORDER:
      if (branch_order == ORDERED_TREE_CHECK_VECTOR_ORDER) {
        return cli_error(argv[0],
                         "--check-order and --reorder are mutually exclusive");
      }
      branch_order = ORDERED_TREE_REORDER_VECTOR_ORDER;
      break;
    default: /* '?' */
      return cli_error(argv[0],
                       "Unknown option or invalid argument; use --name=value");
    }
  }
  if (optind != argc) {
    return cli_error(argv[0],
                     "Unknown option or invalid argument; use --name=value");
  }

  size_t buf_size = 0;
  char *buffer = nullptr;
  if (getline(&buffer, &buf_size, stdin) == -1) {
    free(buffer);
    fputs("Failed to read line!\n", stderr);
    return EXIT_FAILURE;
  }

  OrderedTreeNode *tree = nullptr;
  OrderedTreeError error = {0};
  if (!ordered_tree_parse_leaf_stream_ordered(buffer, branch_order, &tree,
                                              &error)) {
    fprintf(stderr, "Invalid leaf stream at %zu:%zu: %s\n", error.line,
            error.column, error.message);
    free(buffer);
    return EXIT_FAILURE;
  }

  bool wrote_tree = false;
  if (json) {
    fputc('{', stdout);
    json_header(stdout, "strahler-pm/1",
                STRAHLER_TREE_VERSION " (git " STRAHLER_TREE_GIT ")", "prefix",
                argc, argv);
    fputs(",\"tree\":", stdout);
    wrote_tree =
        ordered_tree_write_json(stdout, tree) && fputs("}\n", stdout) >= 0;
  } else {
    wrote_tree = ordered_tree_write_dot(stdout, tree);
  }
  ordered_tree_destroy(tree);
  free(buffer);
  if (!wrote_tree || fflush(stdout) != 0 || ferror(stdout)) {
    fputs(json ? "Failed to write JSON output\n"
               : "Failed to write DOT output\n",
          stderr);
    return EXIT_FAILURE;
  }
  return EXIT_SUCCESS;
}
