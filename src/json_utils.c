#include <inttypes.h>

#include "json_utils.h"

void json_string(FILE *stream, char const *value) {
  fputc('"', stream);
  for (unsigned char const *next = (unsigned char const *)value; *next != 0;
       next++) {
    if (*next == '"' || *next == '\\') {
      fputc('\\', stream);
      fputc(*next, stream);
    } else if (*next < 32) {
      fprintf(stream, "\\u%04x", (unsigned int)*next);
    } else {
      fputc(*next, stream);
    }
  }
  fputc('"', stream);
}

void json_set(JSONWriter const *writer, PGSet const *vertices) {
  fputc('[', writer->stream);
  bool first = true;
  if (vertices != nullptr) {
    for (size_t vertex = pg_set_next(vertices, 0); vertex != SIZE_MAX;
         vertex = pg_set_next(vertices, vertex + 1)) {
      fprintf(writer->stream, "%s%" PRIu64, first ? "" : ",",
              writer->game->vertices[vertex].external_id);
      first = false;
    }
  }
  fputc(']', writer->stream);
}

void json_header(FILE *stream, char const *schema, char const *version,
                 char const *algorithm, int const argc, char *const argv[]) {
  fputs("\"schema\":", stream);
  json_string(stream, schema);
  fputs(",\"version\":", stream);
  json_string(stream, version);
  fputs(",\"algorithm\":", stream);
  json_string(stream, algorithm);
  fputs(",\"options\":[", stream);
  for (int index = 1; index < argc; index++) {
    if (index != 1) {
      fputc(',', stream);
    }
    json_string(stream, argv[index]);
  }
  fputc(']', stream);
}

void json_game(FILE *stream, PGGame const *game, PGPriorityMap const *map) {
  fprintf(stream, "{\"vertices\":%zu,\"edges\":%zu,\"priorities\":[",
          game->vertex_count, game->edge_count);
  for (size_t index = 0; index < map->count; index++) {
    fprintf(stream, "%s%" PRIu64, index == 0 ? "" : ",",
            map->entries[index].original);
  }
  fputs("]}", stream);
}
