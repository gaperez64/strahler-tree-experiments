#include <inttypes.h>

#include "pg_dot.h"

bool pg_dot_write_set(FILE *stream, PGGame const *game, PGSet const *set,
                      size_t const max_items) {
  if (fputc('{', stream) == EOF) {
    return false;
  }
  size_t shown = 0;
  size_t const total = pg_set_count(set);
  for (size_t vertex = pg_set_next(set, 0);
       vertex != SIZE_MAX && shown < max_items;
       vertex = pg_set_next(set, vertex + 1)) {
    if ((shown != 0 && fputc(',', stream) == EOF) ||
        fprintf(stream, "%" PRIu64, game->vertices[vertex].external_id) < 0) {
      return false;
    }
    shown++;
  }
  if (shown < total && fprintf(stream, "%s..., +%zu more",
                               shown == 0 ? "" : ",", total - shown) < 0) {
    return false;
  }
  return fputc('}', stream) != EOF;
}
