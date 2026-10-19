#include <assert.h>
#include <stdio.h>
#include <string.h>

#include "ad_lift_solve.h"
#include "pg_preprocess.h"
#include "reference_solver.h"
#include "zielonka.h"

[[nodiscard]] static PGGame read_game(FILE *stream) {
  assert(fseek(stream, 0, SEEK_SET) == 0);
  PGGame game = {0};
  PGParseError error = {0};
  assert(pg_game_read(stream, &game, &error));
  assert(fclose(stream) == 0);
  return game;
}

[[nodiscard]] static PGGame parse(char const *text) {
  FILE *stream = tmpfile();
  assert(stream != nullptr);
  assert(fwrite(text, 1, strlen(text), stream) == strlen(text));
  return read_game(stream);
}

static void test_options(void) {
  PGPreprocessOptions options = {0};
  assert(pg_preprocess_parse_option(&options, "shave", "wcwc,loops,single"));
  assert(options.shave == PG_SHAVE_ALL);
  assert(pg_preprocess_parse_option(&options, "compress", nullptr));
  assert(options.compress);
  char const *invalid[] = {"",          "bad",         "loops,",
                           ",single",   "loops,,wcwc", "all,loops",
                           "none,wcwc", " loops",      "Loops"};
  for (size_t index = 0; index < sizeof(invalid) / sizeof(invalid[0]);
       index++) {
    assert(!pg_preprocess_parse_option(&options, "shave", invalid[index]));
    assert(options.shave == PG_SHAVE_ALL && options.compress);
  }
  assert(!pg_preprocess_parse_option(&options, "shave", nullptr));
  assert(!pg_preprocess_parse_option(&options, "compress", "yes"));
  assert(!pg_preprocess_parse_option(&options, "unknown", "all"));
  assert(!pg_preprocess_parse_option(nullptr, "shave", "all"));
  assert(!pg_preprocess_parse_option(&options, nullptr, "all"));
  assert(pg_preprocess_parse_option(&options, "shave", "none"));
  assert(options.shave == 0);
  assert(pg_preprocess_parse_option(&options, "shave", "all"));
  assert(pg_preprocess_parse_option(&options, "shave", "loops,loops"));
  assert(options.shave == (1U << PG_SHAVE_LOOPS));
}

static void test_rules(void) {
  char const *paths[] = {"tests/games/shave_single.pg",
                         "tests/games/shave_loops.pg",
                         "tests/games/shave_wcwc.pg"};
  size_t const expected[][3] = {{3, 0, 0}, {3, 1, 2}, {4, 3, 2}};
  for (size_t rule = 0; rule < PG_SHAVE_RULE_COUNT; rule++) {
    FILE *stream = fopen(paths[rule], "rb");
    assert(stream != nullptr);
    PGGame game = read_game(stream);
    PGPreprocessOptions const options = {.shave = 1U << rule};
    PGPreprocessResult result = {0};
    assert(pg_preprocess(&game, &options, &result));
    assert(pg_preprocess_verify(&game, &result));
    for (size_t player = 0; player < 2; player++) {
      assert(pg_set_count(&result.won[player]) == expected[rule][player]);
      assert(result.shaved[rule][player] == expected[rule][player]);
    }
    assert(pg_set_count(&result.active) == expected[rule][2]);
    if (rule == PG_SHAVE_LOOPS) {
      /* Attractor closure must hold in the full graph, including exits from
       * shaved opponent vertices and newly attractable predecessors. */
      pg_set_remove(&result.won[PG_EVEN], 3);
      pg_set_add(&result.active, 3);
      assert(!pg_preprocess_verify(&game, &result));
      pg_set_remove(&result.active, 3);
      pg_set_add(&result.won[PG_ODD], 3);
      assert(!pg_preprocess_verify(&game, &result));
    }
    pg_preprocess_destroy(&result);
    pg_game_destroy(&game);
  }

  /* A losing maximum must not hide a smaller winning cycle; an opponent
   * vertex in a mixed-owner cycle must not be treated as controlled. */
  PGGame game = parse("0 2 0 1,2;\n1 0 0 0;\n2 3 0 0;\n"
                      "3 5 0 4;\n4 4 1 3;\n");
  PGPreprocessOptions options = {.shave = 1U << PG_SHAVE_WCWC};
  PGPreprocessResult result = {0};
  assert(pg_preprocess(&game, &options, &result));
  assert(pg_set_count(&result.won[PG_EVEN]) == 3);
  assert(pg_set_count(&result.active) == 2);
  assert(pg_preprocess_verify(&game, &result));
  pg_preprocess_destroy(&result);
  pg_game_destroy(&game);

  /* Removing an Odd cycle leaves only even priorities: single runs again. */
  game = parse("0 1 1 1;\n1 1 1 0;\n2 2 0 3;\n3 0 1 2;\n");
  options.shave = PG_SHAVE_ALL;
  assert(pg_preprocess(&game, &options, &result));
  assert(pg_set_empty(&result.active));
  assert(result.shaved[PG_SHAVE_WCWC][PG_ODD] == 2);
  assert(result.shaved[PG_SHAVE_SINGLE][PG_EVEN] == 2);
  assert(pg_preprocess_verify(&game, &result));
  pg_preprocess_destroy(&result);
  pg_game_destroy(&game);

  /* A loop visited earlier becomes forced after another loop is removed. */
  game = parse("0 1 0 0,1;\n1 3 1 1;\n2 2 1 2,3;\n3 1 0 2;\n");
  options.shave = 1U << PG_SHAVE_LOOPS;
  assert(pg_preprocess(&game, &options, &result));
  assert(result.shaved[PG_SHAVE_LOOPS][PG_ODD] == 2);
  assert(pg_set_count(&result.active) == 2);
  assert(pg_preprocess_verify(&game, &result));
  pg_preprocess_destroy(&result);
  pg_game_destroy(&game);
}

static void test_compression(void) {
  FILE *stream = fopen("tests/games/compress.pg", "rb");
  assert(stream != nullptr);
  PGGame game = read_game(stream);
  PGPreprocessOptions const options = {.compress = true};
  PGPreprocessResult result = {0};
  assert(pg_preprocess(&game, &options, &result));
  uint64_t const priorities[] = {0, 0, 0, 1, 1, 2};
  for (size_t vertex = 0; vertex < game.vertex_count; vertex++) {
    assert(game.vertices[vertex].priority == priorities[vertex]);
  }
  uint64_t bound = 0;
  assert(pg_priority_map_original_bound(&result.priority_map, 0, &bound));
  assert(bound == 100);
  assert(pg_priority_map_original_bound(&result.priority_map, 1, &bound));
  assert(bound == 107);
  assert(pg_priority_map_original_bound(&result.priority_map, 2, &bound));
  assert(bound == 200);
  assert(pg_priority_map_original_bound(&result.priority_map, 3, &bound));
  assert(bound == 201);
  assert(pg_preprocess_verify(&game, &result));
  pg_preprocess_destroy(&result);
  pg_game_destroy(&game);

  game = parse("0 1 0 0;\n1 7 1 1;\n2 8 0 2;\n3 12 1 3;\n");
  assert(pg_preprocess(&game, &options, &result));
  assert(game.vertices[0].priority == 1 && game.vertices[1].priority == 1);
  assert(game.vertices[2].priority == 2 && game.vertices[3].priority == 2);
  assert(pg_priority_map_original_bound(&result.priority_map, 0, &bound));
  assert(bound == 0);
  assert(pg_priority_map_original_bound(&result.priority_map, 1, &bound));
  assert(bound == 7);
  pg_preprocess_destroy(&result);
  pg_game_destroy(&game);
}

static uint32_t random_state = UINT32_C(0xc0ffee);

[[nodiscard]] static uint32_t next_random(void) {
  random_state = random_state * UINT32_C(1664525) + UINT32_C(1013904223);
  return random_state;
}

static void test_reference_agreement(void) {
  for (size_t iteration = 0; iteration < 120; iteration++) {
    size_t const count = 2 + (next_random() >> 16) % 4;
    FILE *stream = tmpfile();
    assert(stream != nullptr);
    for (size_t vertex = 0; vertex < count; vertex++) {
      unsigned const priority = (next_random() >> 16) % 8;
      unsigned const owner = (next_random() >> 8) % 2;
      size_t const first = (next_random() >> 16) % count;
      size_t const second = (next_random() >> 16) % count;
      assert(fprintf(stream, "%zu %u %u %zu,%zu;\n", vertex, priority, owner,
                     first, second) > 0);
    }
    PGGame game = read_game(stream);
    PGSet reference[2] = {0};
    assert(reference_solve(&game, &reference[0], &reference[1]));
    PGPreprocessOptions const options = {
        .shave = (unsigned)(iteration % (PG_SHAVE_ALL + 1)),
        .compress = iteration % 3 != 0,
    };
    PGPreprocessResult result = {0};
    assert(pg_preprocess(&game, &options, &result));
    assert(pg_preprocess_verify(&game, &result));
    ADResult residual = {0};
    ZielonkaError error = {0};
    assert(zielonka_decompose(&game, &result.active, game.max_priority,
                              &residual, &error));
    ADVerifyError verify_error = {0};
    assert(ad_result_verify_complete(&game, &result.active, &residual,
                                     &verify_error));
    for (size_t player = 0; player < 2; player++) {
      assert(pg_set_subset(&result.won[player], &reference[player]));
      pg_set_union_into(&residual.region[player], &result.won[player]);
      assert(pg_set_equal(&residual.region[player], &reference[player]));
    }
    ad_result_destroy(&residual);

    ADLiftOptions const lift_options = {
        .mode = AD_LIFT_HOST_FULL,
        .max_host_leaves = 10000,
        .verify = true,
    };
    ADLiftError lift_error = {0};
    assert(ad_lift_solve(&game, &result.active, &lift_options, &residual,
                         nullptr, &lift_error));
    assert(residual.kind == AD_RESULT_COMPLETE);
    for (size_t player = 0; player < 2; player++) {
      pg_set_union_into(&residual.region[player], &result.won[player]);
      assert(pg_set_equal(&residual.region[player], &reference[player]));
      pg_set_destroy(&reference[player]);
    }
    ad_result_destroy(&residual);
    pg_preprocess_destroy(&result);
    pg_game_destroy(&game);
  }
}

static void test_scaling(PGPreprocessOptions const *options) {
  size_t const count = 100000;
  for (size_t shape = 0; shape < 2; shape++) {
    bool const loops = shape == 0;
    FILE *stream = tmpfile();
    assert(stream != nullptr);
    for (size_t vertex = 0; vertex < count; vertex++) {
      unsigned const owner = (unsigned)(vertex % 2);
      unsigned priority = owner;
      size_t to = vertex;
      if (!loops) {
        /* Candidates lead to a mixed-owner cycle with no controlled cycle. */
        to = count - 2 + owner;
        if (vertex >= count - 2) {
          priority = 1 - owner;
          to = count - 2 + (1 - owner);
        }
      }
      assert(fprintf(stream, "%zu %u %u %zu;\n", vertex, priority, owner, to) >
             0);
    }
    PGGame game = read_game(stream);
    PGPreprocessResult result = {0};
    assert(pg_preprocess(&game, options, &result));
    assert(pg_preprocess_verify(&game, &result));
    assert(pg_set_count(&result.active) == (loops ? 0 : count));
    for (size_t player = 0; player < 2; player++) {
      assert(pg_set_count(&result.won[player]) == (loops ? count / 2 : 0));
    }
    pg_preprocess_destroy(&result);
    pg_game_destroy(&game);
  }
}

int main(int argc, char **argv) {
  if (argc == 2) {
    PGPreprocessOptions options = {0};
    assert(pg_preprocess_parse_option(&options, "shave", argv[1]));
    test_scaling(&options);
    return 0;
  }
  assert(argc == 1);
  test_options();
  test_rules();
  test_compression();
  test_reference_agreement();
  return 0;
}
