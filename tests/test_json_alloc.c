#include <assert.h>
#include <errno.h>
#include <stdlib.h>

#include "ad_tree_json.h"
#include "ordered_tree.h"
#include "pm_tree_dot.h"
#include "zielonka.h"

#undef malloc
#undef calloc
#undef realloc

static size_t allocation;
static size_t fail_at = SIZE_MAX;

void *trace_test_malloc(size_t const size) {
  if (++allocation == fail_at) {
    errno = ENOMEM;
    return nullptr;
  }
  return malloc(size);
}

void *trace_test_calloc(size_t const count, size_t const size) {
  if (++allocation == fail_at) {
    errno = ENOMEM;
    return nullptr;
  }
  return calloc(count, size);
}

void *trace_test_realloc(void *data, size_t const size) {
  if (++allocation == fail_at) {
    errno = ENOMEM;
    return nullptr;
  }
  return realloc(data, size);
}

int main(void) {
  FILE *input = tmpfile();
  assert(input != nullptr);
  assert(fputs("0 2 0 0;1 0 0 1;2 1 0 0;", input) >= 0);
  assert(fseek(input, 0, SEEK_SET) == 0);
  PGGame game = {0};
  PGParseError parse = {0};
  assert(pg_game_read(input, &game, &parse));
  assert(fclose(input) == 0);
  PGSet active = {0};
  assert(pg_set_init(&active, game.vertex_count));
  pg_set_fill(&active);
  PGSet shaved[2] = {0};
  assert(pg_set_init(shaved, game.vertex_count));
  assert(pg_set_init(shaved + 1, game.vertex_count));
  ADResult result = {0};
  ZielonkaError error = {0};
  assert(zielonka_decompose(&game, &active, 2, &result, &error));
  PMResult measures[2] = {0};
  PMError pm_error = {0};
  for (size_t player = 0; player < 2; player++) {
    assert(pm_lift(&game, &active, PM_STRAHLER, (PMParameters){.k = 2, .t = 1},
                   (PGPlayer)player, &measures[player], &pm_error));
  }
  for (size_t scenario = 0; scenario < 3; scenario++) {
    bool completed = false;
    for (size_t nth = 1; nth < 1000; nth++) {
      FILE *out = tmpfile();
      assert(out != nullptr);
      allocation = 0;
      fail_at = nth;
      errno = 0;
      bool success = false;
      if (scenario == 0) {
        success = ad_json_metrics(out, &result, AD_DOT_PLAYER_BOTH);
      } else if (scenario == 1) {
        success = pm_write_json(out, &game, measures, &result.unresolved, 1,
                                AD_DOT_PLAYER_BOTH, nullptr, shaved);
      } else {
        OrderedTreeNode *tree = nullptr;
        OrderedTreeError tree_error = {0};
        success =
            ordered_tree_parse_leaf_stream("0,e|1,e|", &tree, &tree_error);
        if (success) {
          success = ordered_tree_write_json(out, tree);
        }
        ordered_tree_destroy(tree);
      }
      int const saved_errno = errno;
      fail_at = SIZE_MAX;
      assert(fclose(out) == 0);
      if (success) {
        assert(allocation < nth);
        completed = true;
        break;
      }
      assert(allocation >= nth && saved_errno == ENOMEM);
    }
    assert(completed);
  }
  /* Read-only /dev/null gives a portable write failure, including on macOS. */
  FILE *out = fopen("/dev/null", "r");
  assert(out != nullptr);
  assert(setvbuf(out, nullptr, _IONBF, 0) == 0);
  assert(
      !ad_json_result(&(JSONWriter){out, &game}, &result, AD_DOT_PLAYER_BOTH));
  assert(!ad_json_metrics(out, &result, AD_DOT_PLAYER_BOTH));
  assert(!pm_write_json(out, &game, measures, &result.unresolved, 1,
                        AD_DOT_PLAYER_BOTH, nullptr, shaved));
  OrderedTreeNode *tree = nullptr;
  OrderedTreeError tree_error = {0};
  assert(ordered_tree_parse_leaf_stream("0,e|1,e|", &tree, &tree_error));
  assert(!ordered_tree_write_json(out, tree));
  ordered_tree_destroy(tree);
  assert(fclose(out) == 0);
  for (size_t player = 0; player < 2; player++) {
    pm_result_destroy(&measures[player]);
    pg_set_destroy(&shaved[player]);
  }
  ad_result_destroy(&result);
  pg_set_destroy(&active);
  pg_game_destroy(&game);
  return 0;
}
