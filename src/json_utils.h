#ifndef JSON_UTILS_H
#define JSON_UTILS_H 1

#include "pg_game.h"
#include "pg_set.h"

typedef struct {
  FILE *stream;
  PGGame const *game;
} JSONWriter;

/* Stream fragments; callers check ferror and flush the completed document. */
void json_string(FILE *stream, char const *value);
void json_set(JSONWriter const *writer, PGSet const *vertices);
void json_header(FILE *stream, char const *schema, char const *version,
                 char const *algorithm, int argc, char *const argv[]);
void json_game(FILE *stream, PGGame const *game, PGPriorityMap const *map);

#endif
