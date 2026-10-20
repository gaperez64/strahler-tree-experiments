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
[[nodiscard]] int cli_error(char const *program_path, char const *message);
[[nodiscard]] int cli_print_version(char const *program_path);

#ifdef __cplusplus
}
#endif

#endif
