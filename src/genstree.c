#define _POSIX_C_SOURCE 200809L

#include <assert.h>
#include <errno.h>
#include <getopt.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cli_version.h"
#include "json_utils.h"
#include "ordered_tree.h"
#include "strahler_tree_version.h"
#include "stree.h"
#include "utrees.h"

[[nodiscard]] static bool parse_int(char const *text, int minimum,
                                    int *result) {
  assert(text != nullptr);
  assert(result != nullptr);

  errno = 0;
  char *end = nullptr;
  long const value = strtol(text, &end, 10);
  if (text[0] == '\0' || strspn(text, "0123456789") != strlen(text) ||
      errno == ERANGE || end == text || *end != '\0' || value < minimum ||
      value > INT_MAX) {
    return false;
  }

  *result = (int)value;
  return true;
}

static void print_usage(FILE *out, char *argv[]) {
  cli_usage(out, argv[0], "");
  fputs("  --strahler=K                                Strahler parameter "
        "(required, 1 <= K <= H)\n"
        "  --height=H                                  Tree height (required, "
        "H >= 1)\n"
        "  --log-leaves=T                              Leaf-budget exponent "
        "(required, T >= 0)\n"
        "  --count                                     Print only the leaf "
        "count (default: leaf labels)\n"
        "  --leaf=L                                    Print the L-th leaf "
        "(1-based)\n"
        "  --dot                                       Print the tree in DOT "
        "format (default: off)\n"
        "  --json                                      Print the tree as JSON\n"
        "  --p-level=P                                 Print the partition at "
        "p-level P (P >= 1)\n"
        "With --p-level or no output option, leaf labels are printed.\n",
        out);
}

static void print_bits(char const labels[static 1]) {
  assert(labels != nullptr);
  bool first = true;

  puts("Bits:");
  for (char const *cur = labels; *cur != '\0'; cur++) {
    switch (*cur) {
    case ZERO:
    case ONE:
      printf(first ? "{%c" : ", %c", *cur);
      first = false;
      break;
    case EPSILON:
    case COMMA:
      break;
    case EOS:
      if (first) {
        fputs("{ ", stdout);
      }
      puts("}");
      first = true;
      break;
    default:
      assert(false);
    }
  }
}

static void print_blocks(char const labels[static 1]) {
  assert(labels != nullptr);
  unsigned block = 0;
  bool first = true;

  puts("Blocks:");
  for (char const *cur = labels; *cur != '\0'; cur++) {
    switch (*cur) {
    case ZERO:
    case ONE:
      printf(first ? "{%u" : ", %u", block);
      first = false;
      break;
    case EPSILON:
      break;
    case COMMA:
      block++;
      break;
    case EOS:
      if (first) {
        fputs("{ ", stdout);
      }
      puts("}");
      block = 0;
      first = true;
      break;
    default:
      assert(false);
    }
  }
}

[[nodiscard]] static OrderedTreeNode *parse_generated_tree(char const *labels) {
  OrderedTreeNode *tree = nullptr;
  OrderedTreeError error = {0};
  if (!ordered_tree_parse_leaf_stream(labels, &tree, &error)) {
    fprintf(stderr, "Generated an invalid tree at %zu:%zu: %s\n", error.line,
            error.column, error.message);
    return nullptr;
  }
  return tree;
}

int main(int argc, char *argv[argc + 1]) {
  static struct option const long_options[] = {
      {"help", no_argument, nullptr, 1},
      {"version", no_argument, nullptr, 'v'},
      {"strahler", required_argument, nullptr, 'k'},
      {"log-leaves", required_argument, nullptr, 't'},
      {"height", required_argument, nullptr, 'h'},
      {"count", no_argument, nullptr, 'j'},
      {"leaf", required_argument, nullptr, 'l'},
      {"json", no_argument, nullptr, 'J'},
      {"dot", no_argument, nullptr, 'd'},
      {"p-level", required_argument, nullptr, 'p'},
      {nullptr, 0, nullptr, 0},
  };

  int k = 0;
  int t = 0;
  int h = 0;
  int p = 0;
  int leaf_number = 0;
  bool k_set = false;
  bool t_set = false;
  bool h_set = false;
  bool just_count = false;
  bool print_dot = false;
  bool json = false;

  int option = 0;
  while ((option = cli_getopt(argc, argv, long_options)) != -1) {
    switch (option) {
    case 'v':
      return cli_print_version(argv[0]);
    case 1:
      print_usage(stdout, argv);
      return EXIT_SUCCESS;
    case 'l':
      if (!parse_int(optarg, 1, &leaf_number)) {
        return cli_error(argv[0], "--leaf must be a positive integer");
      }
      break;
    case 'j':
      just_count = true;
      break;
    case 'J':
      json = true;
      break;
    case 'd':
      print_dot = true;
      break;
    case 'p':
      if (!parse_int(optarg, 1, &p)) {
        return cli_error(argv[0], "--p-level must be a positive integer");
      }
      break;
    case 'k':
      if (!parse_int(optarg, 1, &k)) {
        return cli_error(argv[0], "--strahler must be a positive integer");
      }
      k_set = true;
      break;
    case 't':
      if (!parse_int(optarg, 0, &t)) {
        return cli_error(argv[0], "--log-leaves must be a nonnegative integer");
      }
      t_set = true;
      break;
    case 'h':
      if (!parse_int(optarg, 1, &h)) {
        return cli_error(argv[0], "--height must be a positive integer");
      }
      h_set = true;
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

  if (!(k_set && t_set && h_set)) {
    return cli_error(argv[0],
                     "--strahler, --log-leaves and --height are required");
  }
  if (h < k) {
    return cli_error(argv[0], "--height must be at least --strahler");
  }

  if (json && (just_count || print_dot || leaf_number > 0 || p > 0)) {
    return cli_error(argv[0], "--json is mutually exclusive with --count, "
                              "--leaf, --dot and --p-level");
  }

  unsigned const total = stree_count_leaves(k, t, h);
  if (total == 0) {
    fputs("Failed to construct the leaf-count cache\n", stderr);
    return EXIT_FAILURE;
  }

  if (leaf_number > 0) {
    if ((unsigned)leaf_number > total) {
      return cli_error(argv[0], "--leaf exceeds the number of leaves");
    }
    if (total == UINT_MAX) {
      fputs("The tree has too many leaves to index\n", stderr);
      return EXIT_FAILURE;
    }
    char *label = stree_leaf_label(k, t, h, leaf_number);
    if (label == nullptr) {
      fputs("Failed to allocate leaf label\n", stderr);
      return EXIT_FAILURE;
    }
    print_bits(label);
    print_blocks(label);
    free(label);
    return EXIT_SUCCESS;
  }

  if (just_count) {
    printf("U^%d_{%d,%d} has %s%u leaves\n", k, t, h,
           total == UINT_MAX ? "at least " : "", total);
    return EXIT_SUCCESS;
  }

  char *labels = stree_leaf_stream(k, t, h);
  if (labels == nullptr) {
    fputs("Failed to allocate leaf labels\n", stderr);
    return EXIT_FAILURE;
  }

  int result = EXIT_SUCCESS;
  if (print_dot || json || p > 0) {
    OrderedTreeNode *tree = parse_generated_tree(labels);
    if (tree == nullptr) {
      free(labels);
      return EXIT_FAILURE;
    }
    if (json) {
      fputc('{', stdout);
      json_header(stdout, "strahler-tree/1",
                  STRAHLER_TREE_VERSION " (git " STRAHLER_TREE_GIT ")",
                  "strahler", argc, argv);
      fprintf(stdout,
              ",\"parameters\":{\"k\":%d,\"h\":%d,\"t\":%d},\"tree\":", k, h,
              t);
      result =
          ordered_tree_write_json(stdout, tree) && fputs("}\n", stdout) >= 0
              ? EXIT_SUCCESS
              : EXIT_FAILURE;
    } else if (print_dot) {
      result =
          ordered_tree_write_dot(stdout, tree) ? EXIT_SUCCESS : EXIT_FAILURE;
    } else {
      print_bits(labels);
      print_blocks(labels);
      result = ordered_tree_write_p_partition(stdout, tree, (unsigned)p)
                   ? EXIT_SUCCESS
                   : EXIT_FAILURE;
    }
    ordered_tree_destroy(tree);
  } else {
    print_bits(labels);
    print_blocks(labels);
  }
  free(labels);
  return result == EXIT_SUCCESS && fflush(stdout) == 0 && !ferror(stdout)
             ? EXIT_SUCCESS
             : EXIT_FAILURE;
}
