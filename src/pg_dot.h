#ifndef PG_DOT_H
#define PG_DOT_H 1

#include "pg_game.h"
#include "pg_set.h"

[[nodiscard]] bool pg_dot_write_set(FILE *stream, PGGame const *game,
                                    PGSet const *set, size_t max_items);

#endif
