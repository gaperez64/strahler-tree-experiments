#ifndef PG_GAME_INTERNAL_H
#define PG_GAME_INTERNAL_H 1

#include "pg_game.h"

#define PG_GAME_DEFAULT_CHUNK ((size_t)65536)

/* Internal parser test entry point; the public reader uses the default chunk.
 */
[[nodiscard]]
bool pg_game_read_chunked(FILE *input, size_t chunk, PGGame *game,
                          PGParseError *error);

#ifdef PG_GAME_TEST_ALLOCATOR
void *pg_game_test_malloc(size_t size);
void *pg_game_test_calloc(size_t count, size_t size);
void *pg_game_test_realloc(void *data, size_t size);
#endif

#endif
