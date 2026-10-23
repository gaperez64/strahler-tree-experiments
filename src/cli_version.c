#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cli_version.h"
#include "strahler_tree_version.h"

static char const *program_name(char const *path) {
  char const *slash = strrchr(path, '/');
  return slash == nullptr ? path : slash + 1;
}

static bool valid_options(int argc, char *argv[],
                          struct option const options[]) {
  for (int i = 1; i < argc; i++) {
    char const *argument = argv[i];
    if (strcmp(argument, "--") == 0) {
      break;
    }
    if (argument[0] != '-' || argument[1] == '\0') {
      continue;
    }
    if (argument[1] != '-') {
      return false;
    }
    size_t const length = strcspn(argument + 2, "=");
    struct option const *option = options;
    while (option->name != nullptr &&
           (strlen(option->name) != length ||
            strncmp(option->name, argument + 2, length) != 0)) {
      option++;
    }
    bool const has_value = argument[length + 2] == '=';
    if (option->name == nullptr ||
        (option->has_arg == required_argument && !has_value) ||
        (option->has_arg == no_argument && has_value)) {
      return false;
    }
  }
  return true;
}

int cli_getopt(int argc, char *argv[], struct option const options[]) {
  if (optind == 1) {
    opterr = 0;
    if (!valid_options(argc, argv, options)) {
      return '?';
    }
  }
  return getopt_long(argc, argv, "", options, nullptr);
}

void cli_usage(FILE *out, char const *program_path, char const *operands) {
  fprintf(out,
          "Usage: %s [OPTIONS]%s\n\n"
          "Option values use --name=value.\n\n"
          "Options:\n"
          "  --help                                      Print this message\n"
          "  --version                                   Print the program "
          "version\n",
          program_name(program_path), operands);
}

int cli_error(char const *program_path, char const *message) {
  return cli_error_to(stderr, program_path, message);
}

int cli_error_to(FILE *out, char const *program_path, char const *message) {
  char const *program = program_name(program_path);
  fprintf(out, "%s: %s\nTry '%s --help'.\n", program, message, program);
  return 2;
}

int cli_print_version(char const *program_path) {
  return cli_version_to(stdout, program_path);
}

int cli_version_to(FILE *out, char const *program_path) {
  char const *version = strcmp(STRAHLER_TREE_GIT, "no git") == 0
                            ? STRAHLER_TREE_VERSION
                            : STRAHLER_TREE_VERSION " (git " STRAHLER_TREE_GIT
                                                    ")";
  return fprintf(out, "%s %s\n", program_name(program_path), version) >= 0
             ? EXIT_SUCCESS
             : EXIT_FAILURE;
}

int cli_next_option(int const argc, char *argv[], CLIParser *parser,
                    struct option const options[]) {
  parser->argument = nullptr;
  if (parser->index == 1 && !valid_options(argc, argv, options)) {
    return '?';
  }
  int next = parser->index;
  while (next < argc && (argv[next][0] != '-' || argv[next][1] == '\0')) {
    if (getenv("POSIXLY_CORRECT") != nullptr) {
      return -1;
    }
    next++;
  }
  if (next == argc) {
    return -1;
  }
  char *argument = argv[next];
  // Move options ahead of operands without changing either group's order.
  memmove((void *)(argv + parser->index + 1),
          (void const *)(argv + parser->index),
          (size_t)(next - parser->index) * sizeof(*argv));
  argv[parser->index++] = argument;
  if (strcmp(argument, "--") == 0) {
    return -1;
  }
  if (argument[1] != '-') {
    return '?';
  }
  size_t const length = strcspn(argument + 2, "=");
  bool const has_value = argument[length + 2] == '=';
  for (struct option const *option = options; option->name != nullptr;
       option++) {
    if (strlen(option->name) == length &&
        strncmp(option->name, argument + 2, length) == 0) {
      if ((option->has_arg == required_argument && !has_value) ||
          (option->has_arg == no_argument && has_value)) {
        return '?';
      }
      parser->argument = has_value ? argument + length + 3 : nullptr;
      return option->val;
    }
  }
  return '?';
}
