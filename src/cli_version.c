#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cli_version.h"
#include "strahler_tree_version.h"

static char const *program_name(char const *path) {
  char const *slash = strrchr(path, '/');
  return slash == nullptr ? path : slash + 1;
}

int cli_getopt(int argc, char *argv[], struct option const options[]) {
  if (optind == 1) {
    opterr = 0;
    for (int i = 1; i < argc; i++) {
      char const *argument = argv[i];
      if (strcmp(argument, "--") == 0) {
        break;
      }
      if (argument[0] != '-' || argument[1] == '\0') {
        continue;
      }
      if (argument[1] != '-') {
        return '?';
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
        return '?';
      }
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
  char const *program = program_name(program_path);
  fprintf(stderr, "%s: %s\nTry '%s --help'.\n", program, message, program);
  return 2;
}

int cli_print_version(char const *program_path) {
  char const *version = strcmp(STRAHLER_TREE_GIT, "no git") == 0
                            ? STRAHLER_TREE_VERSION
                            : STRAHLER_TREE_VERSION " (git " STRAHLER_TREE_GIT
                                                    ")";
  return printf("%s %s\n", program_name(program_path), version) >= 0
             ? EXIT_SUCCESS
             : EXIT_FAILURE;
}
