#include "cli_commands.h"

int main(int argc, char *argv[argc + 1]) {
  CLIIO io = {.in = stdin, .out = stdout, .err = stderr};
  return genstree_command(argc, argv, &io);
}
