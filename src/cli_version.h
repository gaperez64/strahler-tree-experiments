#ifndef CLI_VERSION_H
#define CLI_VERSION_H 1

#include <getopt.h>
#include <stdio.h>

#ifdef __cplusplus
extern "C" {
#endif

// Accept exact long names only, with values attached using '='.
[[nodiscard]] int cli_getopt(int argc, char *argv[],
                             struct option const options[]);
void cli_usage(FILE *out, char const *program_path, char const *operands);
typedef struct {
  int index;
  char const *argument;
} CLIParser;

// Reentrant counterpart, also retaining getopt's operand permutation.
int cli_next_option(int argc, char *argv[], CLIParser *parser,
                    struct option const options[]);
int cli_error_to(FILE *out, char const *program_path, char const *message);
int cli_version_to(FILE *out, char const *program_path);
[[nodiscard]] int cli_error(char const *program_path, char const *message);
[[nodiscard]] int cli_print_version(char const *program_path);

#ifdef __cplusplus
}
#endif

#endif
