#ifndef CLI_COMMANDS_H
#define CLI_COMMANDS_H 1

#include "pg_game.h"

typedef struct {
  FILE *in;
  FILE *out;
  FILE *err;
  PGGame const *game;
  bool (*event_callback)(void *context, char const *line, size_t length);
  void *context;
} CLIIO;

int pg2adot_command(int argc, char *argv[], CLIIO *io);
int pg2pmdot_command(int argc, char *argv[], CLIIO *io);
int genstree_command(int argc, char *argv[], CLIIO *io);
int pms2dot_command(int argc, char *argv[], CLIIO *io);
bool cli_game_copy(PGGame const *source, PGGame *destination);

#endif
