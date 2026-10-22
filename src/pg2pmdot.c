#include "cli_commands.h"

int main(int argc, char *argv[argc + 1]) {
  CLIIO io = {.in = stdin, .out = stdout, .err = stderr};
  return pg2pmdot_command(argc, argv, &io);
}
