#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "pg_game_internal.h"

static size_t allocation;
static size_t fail_at;

void *pg_game_test_malloc(size_t const size) {
  return ++allocation == fail_at ? nullptr : malloc(size);
}

void *pg_game_test_calloc(size_t const count, size_t const size) {
  return ++allocation == fail_at ? nullptr : calloc(count, size);
}

void *pg_game_test_realloc(void *data, size_t const size) {
  return ++allocation == fail_at ? nullptr : realloc(data, size);
}

static void check_failures(char const *text) {
  FILE *input = tmpfile();
  assert(input != nullptr);
  size_t const length = strlen(text);
  assert(fwrite(text, 1, length, input) == length);
  for (size_t nth = 1; nth < 1000; nth++) {
    assert(fseek(input, 0, SEEK_SET) == 0);
    allocation = 0;
    fail_at = nth;
    PGGame game = {0};
    PGParseError error = {0};
    bool const parsed = pg_game_read_chunked(input, 7, &game, &error);
    if (parsed) {
      assert(allocation < nth);
      pg_game_destroy(&game);
      assert(fclose(input) == 0);
      return;
    }
    assert(allocation >= nth);
    assert(strstr(error.message, "allocate") != nullptr);
    assert(error.line > 0 && error.column > 0);
    assert(game.vertices == nullptr && game.vertex_count == 0);
    assert(game.edge_count == 0 && game.successors == nullptr);
    assert(game.predecessors == nullptr && game.succ_offsets == nullptr &&
           game.pred_offsets == nullptr);
    pg_game_destroy(&game);
  }
  assert(false);
}

int main(void) {
  check_failures("0 0 0 1,0 \"zero\";1 1 1 0 \"one\";2 2 0 2;"
                 "3 0 0 3;4 1 1 4;5 2 0 5;6 0 1 6;");
  check_failures("9 0 0 999,888 \"obsolete\";1 0 0 9,1;"
                 "9 2 1 1 \"replacement\";");
  check_failures("9 0 0 1;1 2 1 9;");
  char text[8192];
  memcpy(text, "0 0 0 0 \"", 9);
  memset(text + 9, 'x', sizeof(text) - 12);
  memcpy(text + sizeof(text) - 3, "\";", 3);
  check_failures(text);
  return 0;
}
