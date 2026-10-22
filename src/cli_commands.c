#include <stdlib.h>
#include <string.h>

#include "cli_commands.h"

bool cli_game_copy(PGGame const *source, PGGame *destination) {
  PGVertex *vertices =
      malloc((source->vertex_count == 0 ? 1 : source->vertex_count) *
             sizeof(*vertices));
  if (vertices == nullptr) {
    return false;
  }
  memcpy(vertices, source->vertices, source->vertex_count * sizeof(*vertices));
  *destination = *source;
  destination->vertices = vertices;
  return true;
}
