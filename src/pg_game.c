/* LP64, no names: CSR payload is 48 V + 16 E bytes. With geometric
 * growth, sorted-input peak is max(192 V + 16 E, 56 V + 24 E) + 64 KiB + 16;
 * unsorted input adds an 8 V pointer index and may overlap the 8 E predecessor
 * buffer with declarations. V/E count all input declarations/edges, including
 * superseded ones. Allocator/qsort workspace and individually owned names
 * are additional; retained successor capacity adds up to 8 E slack. */
#include <ctype.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "pg_game_internal.h"

#ifdef PG_GAME_TEST_ALLOCATOR
#define malloc pg_game_test_malloc
#define calloc pg_game_test_calloc
#define realloc pg_game_test_realloc
#endif
#include "utils.h"

typedef enum {
  TOKEN_EOF,
  TOKEN_NATURAL,
  TOKEN_KW_PARITY,
  TOKEN_KW_START,
  TOKEN_COMMA,
  TOKEN_SEMICOLON,
  TOKEN_QUOTED_NAME,
  TOKEN_ERROR,
} TokenKind;

typedef struct {
  TokenKind kind;
  uint64_t natural;
  size_t line;
  size_t column;
} Token;

typedef struct {
  FILE *input;
  unsigned char *buffer;
  size_t chunk;
  size_t length;
  size_t offset;
  size_t line;
  size_t column;
  bool ended;
  bool failed;
  char *name;
  PGParseError *error;
} Lexer;

typedef struct {
  uint64_t external_id;
  uint64_t priority;
  PGPlayer owner;
  char *name;
  size_t first_successor;
  size_t successor_count;
  size_t line;
  size_t column;
} TempDeclaration;

typedef struct {
  Lexer lexer;
  Token token;
  TempDeclaration *declarations;
  size_t declaration_count;
  size_t declaration_capacity;
  uint64_t *successors;
  size_t successor_count;
  size_t successor_capacity;
  bool sorted;
  bool has_header;
  uint64_t header_maximum;
  uint64_t start_id;
} Parser;

static void set_error(PGParseError *error, size_t const line,
                      size_t const column, char const *message) {
  if (error != nullptr) {
    error->line = line;
    error->column = column;
    (void)snprintf(error->message, sizeof(error->message), "%s", message);
  }
}

[[nodiscard]] static int lexer_peek(Lexer *lexer) {
  if (lexer->offset == lexer->length && !lexer->ended && !lexer->failed) {
    lexer->offset = 0;
    lexer->length = fread(lexer->buffer, 1, lexer->chunk, lexer->input);
    lexer->ended = feof(lexer->input) != 0;
    if (ferror(lexer->input)) {
      lexer->failed = true;
      set_error(lexer->error, 1, 1, "failed to read the input stream");
    }
  }
  return lexer->failed || lexer->offset == lexer->length
             ? EOF
             : lexer->buffer[lexer->offset];
}

static void lexer_advance_byte(Lexer *lexer) {
  if (lexer->buffer[lexer->offset++] == '\n') {
    lexer->line++;
    lexer->column = 1;
  } else {
    lexer->column++;
  }
}

[[nodiscard]] static Token lexer_error(Lexer *lexer, size_t const line,
                                       size_t const column,
                                       char const *message) {
  set_error(lexer->error, line, column, message);
  return (Token){.kind = TOKEN_ERROR, .line = line, .column = column};
}

[[nodiscard]] static Token lexer_next(Lexer *lexer) {
  int byte = lexer_peek(lexer);
  while (byte != EOF && isspace(byte)) {
    lexer_advance_byte(lexer);
    byte = lexer_peek(lexer);
  }
  size_t const line = lexer->line;
  size_t const column = lexer->column;
  Token token = {.line = line, .column = column};
  if (byte == EOF) {
    token.kind = lexer->failed ? TOKEN_ERROR : TOKEN_EOF;
    return token;
  }
  if (isdigit(byte)) {
    uint64_t natural = 0;
    bool overflow = false;
    do {
      unsigned const digit = (unsigned)(byte - '0');
      if (natural > (UINT64_MAX - digit) / 10) {
        overflow = true;
      } else {
        natural = natural * 10 + digit;
      }
      lexer_advance_byte(lexer);
      byte = lexer_peek(lexer);
    } while (byte != EOF && isdigit(byte));
    if (lexer->failed) {
      token.kind = TOKEN_ERROR;
    } else if (overflow) {
      return lexer_error(lexer, line, column,
                         "natural number does not fit in uint64_t");
    } else {
      token.kind = TOKEN_NATURAL;
      token.natural = natural;
    }
    return token;
  }
  if (isalpha(byte)) {
    char word[6];
    size_t length = 0;
    bool too_long = false;
    do {
      if (length < sizeof(word)) {
        word[length++] = (char)byte;
      } else {
        too_long = true;
      }
      lexer_advance_byte(lexer);
      byte = lexer_peek(lexer);
    } while (byte != EOF && isalpha(byte));
    if (lexer->failed) {
      token.kind = TOKEN_ERROR;
    } else if (!too_long && length == 6 && memcmp(word, "parity", 6) == 0) {
      token.kind = TOKEN_KW_PARITY;
    } else if (!too_long && length == 5 && memcmp(word, "start", 5) == 0) {
      token.kind = TOKEN_KW_START;
    } else {
      return lexer_error(lexer, line, column, "unexpected keyword");
    }
    return token;
  }
  lexer_advance_byte(lexer);
  if (byte == ',') {
    token.kind = TOKEN_COMMA;
  } else if (byte == ';') {
    token.kind = TOKEN_SEMICOLON;
  } else if (byte == '"') {
    size_t used = 0;
    size_t capacity = 0;
    while (true) {
      byte = lexer_peek(lexer);
      if (lexer->failed) {
        token.kind = TOKEN_ERROR;
        return token;
      }
      if (byte == EOF) {
        return lexer_error(lexer, line, column, "unterminated quoted name");
      }
      if (byte == 0 || byte > 0x7f) {
        return lexer_error(lexer, lexer->line, lexer->column,
                           "a name must contain only non-NUL ASCII bytes");
      }
      if (used == capacity) {
        ArrayGrowth const growth = grow_array(lexer->name, capacity, 1);
        if (!growth.succeeded) {
          return lexer_error(lexer, line, column,
                             "failed to allocate the node name");
        }
        lexer->name = growth.data;
        capacity = growth.capacity;
      }
      lexer_advance_byte(lexer);
      if (byte == '"') {
        lexer->name[used] = '\0';
        token.kind = TOKEN_QUOTED_NAME;
        break;
      }
      lexer->name[used++] = (char)byte;
    }
  } else {
    return lexer_error(lexer, line, column, "unexpected character");
  }
  return token;
}

static void parser_advance(Parser *parser) {
  if (parser->token.kind != TOKEN_ERROR) {
    parser->token = lexer_next(&parser->lexer);
  }
}

[[nodiscard]] static bool expect(Parser *parser, TokenKind const kind,
                                 char const *message) {
  if (parser->token.kind == kind) {
    return true;
  }
  if (parser->token.kind != TOKEN_ERROR) {
    set_error(parser->lexer.error, parser->token.line, parser->token.column,
              message);
  }
  return false;
}

static void destroy_declarations(TempDeclaration *declarations,
                                 size_t const count) {
  for (size_t index = 0; index < count; index++) {
    free(declarations[index].name);
  }
  free(declarations);
}

[[nodiscard]] static bool append_successor(Parser *parser,
                                           TempDeclaration *declaration,
                                           Token const token) {
  if (parser->successor_count == parser->successor_capacity) {
    ArrayGrowth const growth =
        grow_array(parser->successors, parser->successor_capacity,
                   sizeof(parser->successors[0]));
    if (!growth.succeeded) {
      set_error(parser->lexer.error, token.line, token.column,
                "failed to allocate the successor list");
      return false;
    }
    parser->successors = growth.data;
    parser->successor_capacity = growth.capacity;
  }
  parser->successors[parser->successor_count++] = token.natural;
  declaration->successor_count++;
  return true;
}

[[nodiscard]] static bool append_declaration(Parser *parser,
                                             TempDeclaration *declaration) {
  if (parser->declaration_count == parser->declaration_capacity) {
    ArrayGrowth const growth =
        grow_array(parser->declarations, parser->declaration_capacity,
                   sizeof(parser->declarations[0]));
    if (!growth.succeeded) {
      set_error(parser->lexer.error, declaration->line, declaration->column,
                "failed to allocate the declaration list");
      return false;
    }
    parser->declarations = growth.data;
    parser->declaration_capacity = growth.capacity;
  }
  if (parser->declaration_count != 0 &&
      parser->declarations[parser->declaration_count - 1].external_id >=
          declaration->external_id) {
    parser->sorted = false;
  }
  parser->declarations[parser->declaration_count++] = *declaration;
  *declaration = (TempDeclaration){0};
  return true;
}

[[nodiscard]] static bool parse_declaration(Parser *parser) {
  TempDeclaration declaration = {
      .external_id = parser->token.natural,
      .first_successor = parser->successor_count,
      .line = parser->token.line,
      .column = parser->token.column,
  };
  if (parser->has_header && declaration.external_id > parser->header_maximum) {
    set_error(parser->lexer.error, declaration.line, declaration.column,
              "node identifier exceeds the parity header maximum");
    return false;
  }
  parser_advance(parser);

  if (!expect(parser, TOKEN_NATURAL, "expected a node priority")) {
    goto failure;
  }
  declaration.priority = parser->token.natural;
  parser_advance(parser);

  if (!expect(parser, TOKEN_NATURAL, "expected owner 0 or 1")) {
    goto failure;
  }
  if (parser->token.natural > 1) {
    set_error(parser->lexer.error, parser->token.line, parser->token.column,
              "owner must be exactly 0 or 1");
    goto failure;
  }
  declaration.owner = (PGPlayer)parser->token.natural;
  parser_advance(parser);

  if (!expect(parser, TOKEN_NATURAL,
              "expected at least one successor identifier")) {
    goto failure;
  }
  while (true) {
    Token const successor = parser->token;
    if (parser->has_header && successor.natural > parser->header_maximum) {
      set_error(parser->lexer.error, successor.line, successor.column,
                "successor identifier exceeds the parity header maximum");
      goto failure;
    }
    if (!append_successor(parser, &declaration, successor)) {
      goto failure;
    }
    parser_advance(parser);
    if (parser->token.kind != TOKEN_COMMA) {
      break;
    }
    parser_advance(parser);
    if (!expect(parser, TOKEN_NATURAL,
                "expected a successor identifier after ','")) {
      goto failure;
    }
  }

  if (parser->token.kind == TOKEN_QUOTED_NAME) {
    declaration.name = parser->lexer.name;
    parser->lexer.name = nullptr;
    parser_advance(parser);
  }

  if (!expect(parser, TOKEN_SEMICOLON,
              "expected ';' after the node declaration")) {
    goto failure;
  }
  parser_advance(parser);
  if (!append_declaration(parser, &declaration)) {
    goto failure;
  }
  return true;

failure:
  free(declaration.name);
  return false;
}

[[nodiscard]] static bool parse_stream(Parser *parser) {
  parser->token = lexer_next(&parser->lexer);
  if (parser->token.kind == TOKEN_KW_PARITY) {
    parser->has_header = true;
    parser_advance(parser);
    if (!expect(parser, TOKEN_NATURAL,
                "expected a maximum identifier after 'parity'")) {
      return false;
    }
    parser->header_maximum = parser->token.natural;
    parser_advance(parser);
    if (!expect(parser, TOKEN_SEMICOLON,
                "expected ';' after the parity header")) {
      return false;
    }
    parser_advance(parser);
  }

  if (parser->token.kind == TOKEN_KW_START) {
    parser_advance(parser);
    if (!expect(parser, TOKEN_NATURAL,
                "expected a vertex identifier after 'start'")) {
      return false;
    }
    parser->start_id = parser->token.natural;
    parser_advance(parser);
    if (!expect(parser, TOKEN_SEMICOLON,
                "expected ';' after the start directive")) {
      return false;
    }
    parser_advance(parser);
  }

  while (parser->token.kind != TOKEN_EOF) {
    if (!expect(parser, TOKEN_NATURAL,
                "expected a node declaration or end of input") ||
        !parse_declaration(parser)) {
      return false;
    }
  }
  if (parser->declaration_count == 0) {
    set_error(parser->lexer.error, parser->token.line, parser->token.column,
              "expected at least one node declaration");
    return false;
  }
  return true;
}

[[nodiscard]] static size_t find_vertex(PGGame const *game,
                                        uint64_t const external_id) {
  size_t begin = 0;
  size_t end = game->vertex_count;
  while (begin < end) {
    size_t const middle = begin + (end - begin) / 2;
    uint64_t const candidate = game->vertices[middle].external_id;
    if (candidate < external_id) {
      begin = middle + 1;
    } else {
      end = middle;
    }
  }
  return begin < game->vertex_count &&
                 game->vertices[begin].external_id == external_id
             ? begin
             : SIZE_MAX;
}

[[nodiscard]] static int compare_declarations(void const *left,
                                              void const *right) {
  TempDeclaration const *first = *(TempDeclaration *const *)left;
  TempDeclaration const *second = *(TempDeclaration *const *)right;
  if (first->external_id != second->external_id) {
    return first->external_id < second->external_id ? -1 : 1;
  }
  return first < second ? -1 : first > second ? 1 : 0;
}

/* Sort only pointers; obsolete edge spans are compacted in source order. */
[[nodiscard]] static size_t retain_last_declarations(Parser *parser,
                                                     TempDeclaration **order) {
  size_t const count = parser->declaration_count;
  for (size_t index = 0; index < count; index++) {
    order[index] = parser->declarations + index;
  }
  qsort((void *)order, count, sizeof(TempDeclaration *), compare_declarations);
  size_t retained = 0;
  for (size_t index = 0; index < count; index++) {
    if (index + 1 < count &&
        order[index]->external_id == order[index + 1]->external_id) {
      free(order[index]->name);
      order[index]->name = nullptr;
      order[index]->successor_count = 0;
    } else {
      order[retained++] = order[index];
    }
  }
  size_t used = 0;
  for (size_t index = 0; index < count; index++) {
    TempDeclaration *declaration = parser->declarations + index;
    size_t const length = declaration->successor_count;
    memmove(parser->successors + used,
            parser->successors + declaration->first_successor,
            length * sizeof(parser->successors[0]));
    declaration->first_successor = used;
    used += length;
  }
  parser->successor_count = used;
  return retained;
}

[[nodiscard]] static bool finalize_game(Parser *parser, PGGame *game) {
  PGParseError *error = parser->lexer.error;
  size_t count = parser->declaration_count;
  TempDeclaration **order = nullptr;
  if (!parser->sorted) {
    if (count > SIZE_MAX / sizeof(TempDeclaration *)) {
      set_error(error, 1, 1, "the graph is too large for this platform");
      return false;
    }
    order = (TempDeclaration **)malloc(count * sizeof(TempDeclaration *));
    if (order == nullptr) {
      set_error(error, 1, 1, "failed to allocate the declaration index");
      return false;
    }
    count = retain_last_declarations(parser, order);
  }
  size_t const edges = parser->successor_count;
  if (count > SIZE_MAX / sizeof(game->vertices[0])) {
    set_error(error, 1, 1, "the graph has too many vertices for this platform");
    goto failure;
  }
  if (count >= SIZE_MAX / sizeof(game->succ_offsets[0]) ||
      edges > SIZE_MAX / sizeof(game->successors[0])) {
    set_error(error, 1, 1, "the graph is too large for this platform");
    goto failure;
  }
  game->vertices = calloc(count, sizeof(game->vertices[0]));
  if (game->vertices == nullptr) {
    set_error(error, 1, 1, "failed to allocate graph vertices");
    goto failure;
  }
  game->vertex_count = count;
  game->edge_count = edges;
  game->succ_offsets = calloc(count + 1, sizeof(game->succ_offsets[0]));
  game->pred_offsets = calloc(count + 1, sizeof(game->pred_offsets[0]));
  if (game->succ_offsets == nullptr || game->pred_offsets == nullptr) {
    set_error(error, 1, 1, "failed to allocate the graph edges");
    goto failure;
  }
  bool dense = true;
  for (size_t source = 0; source < count; source++) {
    TempDeclaration *declaration =
        order == nullptr ? parser->declarations + source : order[source];
    game->vertices[source] = (PGVertex){.external_id = declaration->external_id,
                                        .priority = declaration->priority,
                                        .owner = declaration->owner,
                                        .name = declaration->name};
    declaration->name = nullptr;
    if (declaration->external_id != source) {
      dense = false;
    }
    if (declaration->priority > game->max_priority) {
      game->max_priority = declaration->priority;
    }
    /* All offset/count sums are bounded by the checked shared edge count. */
    game->succ_offsets[source + 1] =
        game->succ_offsets[source] + declaration->successor_count;
  }
  game->start_id = parser->start_id;
  game->start_vertex = find_vertex(game, game->start_id);

  bool const reuse = sizeof(size_t) == sizeof(uint64_t);
  if (reuse) {
    game->successors = (void *)parser->successors;
    /* Unsorted edge spans use the eventual predecessor buffer as scratch. */
    if (order != nullptr) {
      game->predecessors = malloc(edges * sizeof(game->predecessors[0]));
    }
  } else {
    game->successors = malloc(edges * sizeof(game->successors[0]));
  }
  if (game->successors == nullptr ||
      (reuse && order != nullptr && game->predecessors == nullptr)) {
    set_error(error, 1, 1, "failed to allocate the graph edges");
    if (reuse) {
      game->successors = nullptr;
    }
    goto failure;
  }
  size_t *targets =
      reuse && order != nullptr ? game->predecessors : game->successors;
  for (size_t source = 0; source < count; source++) {
    TempDeclaration const *declaration =
        order == nullptr ? parser->declarations + source : order[source];
    for (size_t index = 0; index < declaration->successor_count; index++) {
      uint64_t id = 0;
      memcpy(&id, parser->successors + declaration->first_successor + index,
             sizeof(id));
      size_t const target =
          dense ? (id < count ? (size_t)id : SIZE_MAX) : find_vertex(game, id);
      if (target == SIZE_MAX) {
        char message[256];
        (void)snprintf(message, sizeof(message),
                       "successor %" PRIu64 " (position %zu) of node %" PRIu64
                       " has no final declaration",
                       id, index + 1, declaration->external_id);
        set_error(error, declaration->line, declaration->column, message);
        if (reuse) {
          game->successors = nullptr;
        }
        goto failure;
      }
      /* memcpy also permits equal-width, distinct size_t/uint64_t types. */
      memcpy(targets + game->succ_offsets[source] + index, &target,
             sizeof(target));
      game->pred_offsets[target + 1]++;
    }
  }
  if (reuse) {
    if (order != nullptr) {
      memcpy(game->successors, targets, edges * sizeof(targets[0]));
    }
    parser->successors = nullptr;
  }
  free(parser->successors);
  parser->successors = nullptr;
  free((void *)order);
  order = nullptr;
  destroy_declarations(parser->declarations, parser->declaration_count);
  parser->declarations = nullptr;
  parser->declaration_count = 0;

  for (size_t vertex = 0; vertex < count; vertex++) {
    game->pred_offsets[vertex + 1] += game->pred_offsets[vertex];
  }
  if (game->predecessors == nullptr) {
    game->predecessors = malloc(edges * sizeof(game->predecessors[0]));
    if (game->predecessors == nullptr) {
      set_error(error, 1, 1, "failed to allocate the graph edges");
      return false;
    }
  }
  size_t *cursor = malloc(count * sizeof(cursor[0]));
  if (cursor == nullptr) {
    set_error(error, 1, 1, "failed to allocate predecessor cursors");
    return false;
  }
  memcpy(cursor, game->pred_offsets, count * sizeof(cursor[0]));
  for (size_t source = 0; source < count; source++) {
    for (size_t edge = game->succ_offsets[source];
         edge < game->succ_offsets[source + 1]; edge++) {
      game->predecessors[cursor[game->successors[edge]]++] = source;
    }
  }
  free(cursor);
  return true;

failure:
  free((void *)order);
  return false;
}

bool pg_game_read_chunked(FILE *input, size_t const chunk, PGGame *game,
                          PGParseError *error) {
  if (error != nullptr) {
    *error = (PGParseError){.line = 1, .column = 1};
  }
  if (input == nullptr || game == nullptr) {
    set_error(error, 1, 1, "input and game must not be null");
    return false;
  }
  *game = (PGGame){0};
  if (chunk == 0) {
    set_error(error, 1, 1, "input chunk size must be positive");
    return false;
  }
  unsigned char *buffer = malloc(chunk);
  if (buffer == nullptr) {
    set_error(error, 1, 1, "failed to allocate the input buffer");
    return false;
  }
  Parser parser = {.lexer = {.input = input,
                             .buffer = buffer,
                             .chunk = chunk,
                             .line = 1,
                             .column = 1,
                             .error = error},
                   .sorted = true};
  bool const parsed = parse_stream(&parser) && finalize_game(&parser, game);
  if (!parsed) {
    pg_game_destroy(game);
  }
  destroy_declarations(parser.declarations, parser.declaration_count);
  free(parser.successors);
  free(parser.lexer.name);
  free(buffer);
  return parsed;
}

bool pg_game_read(FILE *input, PGGame *game, PGParseError *error) {
  return pg_game_read_chunked(input, PG_GAME_DEFAULT_CHUNK, game, error);
}

void pg_game_destroy(PGGame *game) {
  if (game == nullptr) {
    return;
  }
  for (size_t index = 0; index < game->vertex_count; index++) {
    free(game->vertices[index].name);
  }
  free(game->vertices);
  free(game->succ_offsets);
  free(game->successors);
  free(game->pred_offsets);
  free(game->predecessors);
  *game = (PGGame){0};
}

bool pg_game_write_pgsolver(FILE *out, PGGame const *game,
                            bool const include_names) {
  if (out == nullptr || game == nullptr || game->vertex_count == 0 ||
      game->vertices == nullptr || game->succ_offsets == nullptr ||
      game->successors == nullptr) {
    return false;
  }
  uint64_t const maximum_id =
      game->vertices[game->vertex_count - 1].external_id;
  if (fprintf(out, "parity %" PRIu64 ";\n", maximum_id) < 0) {
    return false;
  }

  for (size_t vertex = 0; vertex < game->vertex_count; vertex++) {
    PGVertex const *data = game->vertices + vertex;
    if (fprintf(out, "%" PRIu64 " %" PRIu64 " %u ", data->external_id,
                data->priority, (unsigned)data->owner) < 0) {
      return false;
    }
    size_t const begin = game->succ_offsets[vertex];
    size_t const end = game->succ_offsets[vertex + 1];
    if (begin >= end || end > game->edge_count) {
      return false;
    }
    for (size_t edge = begin; edge < end; edge++) {
      size_t const successor = game->successors[edge];
      if (successor >= game->vertex_count ||
          (edge != begin && fputc(',', out) == EOF) ||
          fprintf(out, "%" PRIu64, game->vertices[successor].external_id) < 0) {
        return false;
      }
    }
    if (include_names && data->name != nullptr &&
        fprintf(out, " \"%s\"", data->name) < 0) {
      return false;
    }
    if (fputs(";\n", out) < 0) {
      return false;
    }
  }
  return true;
}

[[nodiscard]] static int compare_priorities(void const *left,
                                            void const *right) {
  uint64_t const first = *(uint64_t const *)left;
  uint64_t const second = *(uint64_t const *)right;
  return first < second ? -1 : first > second ? 1 : 0;
}

[[nodiscard]] static size_t find_original_priority(PGPriorityMap const *map,
                                                   uint64_t const priority) {
  size_t begin = 0;
  size_t end = map->count;
  while (begin < end) {
    size_t const middle = begin + (end - begin) / 2;
    if (map->entries[middle].original < priority) {
      begin = middle + 1;
    } else {
      end = middle;
    }
  }
  return begin < map->count && map->entries[begin].original == priority
             ? begin
             : SIZE_MAX;
}

[[nodiscard]] static size_t find_compact_priority(PGPriorityMap const *map,
                                                  uint64_t const priority) {
  size_t begin = 0;
  size_t end = map->count;
  while (begin < end) {
    size_t const middle = begin + (end - begin) / 2;
    if (map->entries[middle].compact < priority) {
      begin = middle + 1;
    } else {
      end = middle;
    }
  }
  return begin < map->count && map->entries[begin].compact == priority
             ? begin
             : SIZE_MAX;
}

bool pg_priority_map_build(PGGame const *game, PGPriorityMap *map) {
  if (map == nullptr) {
    return false;
  }
  *map = (PGPriorityMap){0};
  if (game == nullptr || game->vertex_count == 0 || game->vertices == nullptr ||
      game->vertex_count > SIZE_MAX / sizeof(uint64_t)) {
    return false;
  }

  uint64_t *priorities = malloc(game->vertex_count * sizeof(priorities[0]));
  if (priorities == nullptr) {
    return false;
  }
  for (size_t vertex = 0; vertex < game->vertex_count; vertex++) {
    priorities[vertex] = game->vertices[vertex].priority;
  }
  qsort(priorities, game->vertex_count, sizeof(priorities[0]),
        compare_priorities);

  size_t distinct = 1;
  for (size_t index = 1; index < game->vertex_count; index++) {
    if (priorities[index] != priorities[index - 1]) {
      priorities[distinct++] = priorities[index];
    }
  }
  if (distinct > SIZE_MAX / sizeof(map->entries[0])) {
    free(priorities);
    return false;
  }
  map->entries = malloc(distinct * sizeof(map->entries[0]));
  if (map->entries == nullptr) {
    free(priorities);
    return false;
  }
  map->count = distinct;
  map->entries[0] = (PGPriorityMapEntry){.original = priorities[0],
                                         .compact = priorities[0] % 2};
  for (size_t index = 1; index < distinct; index++) {
    uint64_t compact = map->entries[index - 1].compact;
    uint64_t const parity = priorities[index] % 2;
    if (compact == UINT64_MAX) {
      goto failure;
    }
    compact++;
    if (compact % 2 != parity) {
      if (compact == UINT64_MAX) {
        goto failure;
      }
      compact++;
    }
    map->entries[index] =
        (PGPriorityMapEntry){.original = priorities[index], .compact = compact};
  }
  free(priorities);
  return true;

failure:
  free(priorities);
  pg_priority_map_destroy(map);
  return false;
}

void pg_priority_map_destroy(PGPriorityMap *map) {
  if (map == nullptr) {
    return;
  }
  free(map->entries);
  *map = (PGPriorityMap){0};
}

bool pg_priority_map_apply(PGPriorityMap const *map, PGGame *game) {
  if (map == nullptr || map->entries == nullptr || map->count == 0 ||
      game == nullptr || game->vertices == nullptr || game->vertex_count == 0) {
    return false;
  }
  for (size_t vertex = 0; vertex < game->vertex_count; vertex++) {
    if (find_original_priority(map, game->vertices[vertex].priority) ==
        SIZE_MAX) {
      return false;
    }
  }
  for (size_t vertex = 0; vertex < game->vertex_count; vertex++) {
    size_t const entry =
        find_original_priority(map, game->vertices[vertex].priority);
    game->vertices[vertex].priority = map->entries[entry].compact;
  }
  game->max_priority = map->entries[map->count - 1].compact;
  return true;
}

bool pg_priority_map_restore(PGPriorityMap const *map, PGGame *game) {
  if (map == nullptr || map->entries == nullptr || map->count == 0 ||
      game == nullptr || game->vertices == nullptr || game->vertex_count == 0) {
    return false;
  }
  for (size_t vertex = 0; vertex < game->vertex_count; vertex++) {
    if (find_compact_priority(map, game->vertices[vertex].priority) ==
        SIZE_MAX) {
      return false;
    }
  }
  for (size_t vertex = 0; vertex < game->vertex_count; vertex++) {
    size_t const entry =
        find_compact_priority(map, game->vertices[vertex].priority);
    game->vertices[vertex].priority = map->entries[entry].original;
  }
  game->max_priority = map->entries[map->count - 1].original;
  return true;
}

bool pg_priority_map_original_bound(PGPriorityMap const *map,
                                    uint64_t const compact_bound,
                                    uint64_t *original_bound) {
  if (map == nullptr || map->entries == nullptr || map->count == 0 ||
      original_bound == nullptr) {
    return false;
  }
  if (compact_bound < map->entries[0].compact) {
    *original_bound = compact_bound;
    return true;
  }

  size_t begin = 0;
  size_t end = map->count;
  while (begin < end) {
    size_t const middle = begin + (end - begin) / 2;
    if (map->entries[middle].compact <= compact_bound) {
      begin = middle + 1;
    } else {
      end = middle;
    }
  }
  PGPriorityMapEntry const entry = map->entries[begin - 1];
  uint64_t const difference = compact_bound - entry.compact;
  if (entry.original > UINT64_MAX - difference) {
    return false;
  }
  *original_bound = entry.original + difference;
  return true;
}
