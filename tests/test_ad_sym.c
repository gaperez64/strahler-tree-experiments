#include <assert.h>
#include <stdio.h>
#include <string.h>

#include "ad_lift_solve.h"
#include "pg_preprocess.h"
#include "reference_solver.h"
#include "zielonka.h"

static uint32_t random_state = UINT32_C(0xd1b54a35);

[[nodiscard]] static uint32_t next_random(void) {
  random_state ^= random_state << 13;
  random_state ^= random_state >> 17;
  random_state ^= random_state << 5;
  return random_state;
}

[[nodiscard]] static PGGame read_game(FILE *stream) {
  PGGame game = {0};
  PGParseError error = {0};
  assert(pg_game_read(stream, &game, &error));
  assert(fclose(stream) == 0);
  return game;
}

static void check(PGGame const *game, PGSet const *domain,
                  ADResult const *result, PGSet const expected[2]) {
  ADVerifyError error = {0};
  if (!ad_result_verify_partial(game, domain, result, &error)) {
    fprintf(stderr, "verification: %s\n", error.message);
    assert(false);
  }
  for (size_t player = 0; player < 2; player++) {
    assert(pg_set_subset(result->region + player, expected + player));
    if (result->kind == AD_RESULT_COMPLETE) {
      assert(pg_set_equal(result->region + player, expected + player));
    }
    if (result->decomposition[player] != nullptr) {
      assert(ad_tree_relative_verify(game, result->region + player,
                                     result->decomposition[player], &error));
    }
  }
}

static void compare_solvers(PGGame const *game, PGSet const *domain,
                            PGSet const expected[2], bool const restricted) {
  ADResult result = {0};
  ZielonkaError zielonka_error = {0};
  assert(zielonka_decompose(game, domain, game->max_priority, &result,
                            &zielonka_error));
  check(game, domain, &result, expected);
  assert(result.kind == AD_RESULT_COMPLETE);
  ad_result_destroy(&result);

  ADSymStats stats = {0};
  ADLiftError error = {0};
  if (!ad_sym_solve(game, domain, nullptr, true, &result, &stats, &error)) {
    fprintf(stderr, "symmetric Zielonka: %s\n", error.message);
    assert(pg_game_write_pgsolver(stderr, game, false));
    assert(false);
  }
  check(game, domain, &result, expected);
  assert(result.kind == AD_RESULT_COMPLETE);
  assert(stats.certification_lifts == 0);
  ad_result_destroy(&result);

  for (size_t host = 0; host < (restricted ? 4U : 1U); host++) {
    ADLiftOptions options = {.mode = host == 0 ? AD_LIFT_HOST_FULL
                                               : AD_LIFT_HOST_KARY,
                             .arity = host,
                             .max_host_leaves = 1000000,
                             .verify = true};
    OrderedTreeNode *base = nullptr;
    if (host == 3) {
      uint64_t maximum = 0;
      for (size_t vertex = pg_set_next(domain, 0); vertex != SIZE_MAX;
           vertex = pg_set_next(domain, vertex + 1)) {
        if (game->vertices[vertex].priority > maximum) {
          maximum = game->vertices[vertex].priority;
        }
      }
      if (maximum < 4) {
        continue;
      }
      OrderedTreeError parse_error = {0};
      assert(ordered_tree_parse_leaf_stream("0|1,0|1,1|", &base, &parse_error));
      options.mode = AD_LIFT_HOST_TREE;
      options.tree = base;
    }
    ADResult lifted = {0};
    assert(ad_lift_solve(game, domain, &options, &lifted, nullptr, &error));
    check(game, domain, &lifted, expected);
    options.symmetric = true;
    if (!ad_lift_solve(game, domain, &options, &result, nullptr, &error)) {
      fprintf(stderr, "symmetric lifting: %s\n", error.message);
      assert(pg_game_write_pgsolver(stderr, game, false));
      assert(false);
    }
    check(game, domain, &result, expected);
    for (size_t player = 0; player < 2; player++) {
      /* Both schedules reach the least valid labelling for this host. */
      assert(pg_set_equal(lifted.region + player, result.region + player));
    }
    if (host == 0) {
      assert(result.kind == AD_RESULT_COMPLETE);
    }
    ordered_tree_destroy(base);
    ad_result_destroy(&lifted);
    ad_result_destroy(&result);
  }
}

static void higher_side_entry(void) {
  FILE *stream = tmpfile();
  assert(stream != nullptr);
  assert(fputs("0 1 0 0; 1 0 0 1,0;\n", stream) >= 0);
  assert(fseek(stream, 0, SEEK_SET) == 0);
  PGGame game = read_game(stream);
  PGSet domain = {0};
  assert(pg_set_init(&domain, game.vertex_count));
  pg_set_fill(&domain);
  ADLiftTree hosts[2] = {0};
  ADLiftError error = {0};
  assert(ad_lift_tree_build_full(2, 2, PG_EVEN, 2, hosts, &error));
  assert(ad_lift_tree_build_full(2, 1, PG_ODD, 1, hosts + 1, &error));
  for (size_t algorithm = 0; algorithm < 2; algorithm++) {
    ADResult result = {0};
    ADSymStats stats = {0};
    assert(ad_sym_solve(&game, &domain, algorithm == 0 ? nullptr : hosts, true,
                        &result, &stats, &error));
    /* The Even call on {1} enters with its Odd label at root-side TOP. */
    assert(stats.calls == 2);
    assert(stats.higher_side_calls == 1);
    assert(pg_set_count(result.region + PG_EVEN) == 1);
    assert(pg_set_contains(result.region + PG_EVEN, 1));
    assert(pg_set_count(result.region + PG_ODD) == 1);
    assert(pg_set_contains(result.region + PG_ODD, 0));
    assert(result.kind == AD_RESULT_COMPLETE);
    ad_result_destroy(&result);
  }
  ad_lift_tree_destroy(hosts);
  ad_lift_tree_destroy(hosts + 1);
  pg_set_destroy(&domain);
  pg_game_destroy(&game);
}

static void random_games(void) {
  for (size_t trial = 0; trial < 600; trial++) {
    size_t const count = 1 + next_random() % 12;
    FILE *stream = tmpfile();
    assert(stream != nullptr);
    for (size_t vertex = 0; vertex < count; vertex++) {
      unsigned const priority = next_random() % 7;
      unsigned const owner = next_random() % 2;
      size_t const first = next_random() % count;
      size_t const second = next_random() % count;
      assert(fprintf(stream, "%zu %u %u %zu,%zu;\n", vertex, priority, owner,
                     first, second) > 0);
    }
    assert(fseek(stream, 0, SEEK_SET) == 0);
    PGGame game = read_game(stream);
    PGSet expected[2] = {0};
    assert(reference_solve(&game, expected, expected + 1));
    PGPreprocessOptions const options = {
        .shave = trial % 3 == 0 ? PG_SHAVE_ALL : 0,
        .compress = trial % 2 == 0,
    };
    PGPreprocessResult preprocessed = {0};
    assert(pg_preprocess(&game, &options, &preprocessed));
    assert(pg_preprocess_verify(&game, &preprocessed));
    for (size_t player = 0; player < 2; player++) {
      assert(pg_set_subset(preprocessed.won + player, expected + player));
      pg_set_subtract_into(expected + player, preprocessed.won + player);
    }
    compare_solvers(&game, &preprocessed.active, expected, trial < 120);
    pg_preprocess_destroy(&preprocessed);
    pg_set_destroy(expected);
    pg_set_destroy(expected + 1);
    pg_game_destroy(&game);
  }
}

static void family(char const *path, size_t const expected_baseline,
                   size_t const expected_symmetric) {
  FILE *stream = fopen(path, "r");
  assert(stream != nullptr);
  PGGame game = read_game(stream);
  PGSet domain = {0};
  assert(pg_set_init(&domain, game.vertex_count));
  pg_set_fill(&domain);
  ADResult reference = {0};
  ZielonkaStats baseline = {0};
  ZielonkaError baseline_error = {0};
  assert(zielonka_decompose_stats(&game, &domain, game.max_priority, &reference,
                                  &baseline, &baseline_error));
  ADResult result = {0};
  ADSymStats stats = {0};
  ADLiftError error = {0};
  if (!ad_sym_solve(&game, &domain, nullptr, true, &result, &stats, &error)) {
    fprintf(stderr, "%s: %s\n", path, error.message);
    assert(false);
  }
  for (size_t vertex = 0; vertex < game.vertex_count; vertex++) {
    PGPlayer const winner =
        strstr(path, "_f") != nullptr ? PG_ODD : (PGPlayer)((vertex / 5) % 2);
    assert(pg_set_contains(reference.region + winner, vertex));
  }
  check(&game, &domain, &result, reference.region);
  assert(result.kind == AD_RESULT_COMPLETE);
  assert(baseline.calls == expected_baseline);
  assert(stats.calls == expected_symmetric);
  assert(stats.calls < baseline.calls);
  fprintf(stderr, "%s: zielonka=%zu symmetric=%zu\n", path, baseline.calls,
          stats.calls);
  ad_result_destroy(&reference);
  ad_result_destroy(&result);
  pg_set_destroy(&domain);
  pg_game_destroy(&game);
}

static void invalid_inputs(void) {
  FILE *stream = tmpfile();
  assert(stream != nullptr);
  assert(fputs("0 0 0 0;\n", stream) >= 0);
  assert(fseek(stream, 0, SEEK_SET) == 0);
  PGGame game = read_game(stream);
  PGSet domain = {0};
  assert(pg_set_init(&domain, game.vertex_count));
  pg_set_fill(&domain);
  ADResult result = {0};
  ADLiftError error = {0};
  assert(
      !ad_sym_solve(nullptr, &domain, nullptr, true, &result, nullptr, &error));
  assert(
      !ad_sym_solve(&game, nullptr, nullptr, true, &result, nullptr, &error));
  assert(
      !ad_sym_solve(&game, &domain, nullptr, true, nullptr, nullptr, &error));
  ADLiftTree hosts[2] = {0};
  assert(!ad_sym_solve(&game, &domain, hosts, true, &result, nullptr, &error));
  game.vertices[0].priority = 1025;
  assert(
      !ad_sym_solve(&game, &domain, nullptr, true, &result, nullptr, &error));
  game.vertices[0].priority = 0;
  assert(ad_lift_tree_build_full(1, 1, PG_EVEN, 0, hosts, &error));
  ADLiftLabelling labelling = {0};
  assert(!ad_lift_continue(&game, &domain, hosts, &labelling, &error));
  assert(ad_lift_run(&game, &domain, hosts, AD_LIFT_SCHEDULE_ROUNDS, &labelling,
                     &error));
  labelling.labels[0] = SIZE_MAX;
  assert(!ad_lift_continue(&game, &domain, hosts, &labelling, &error));
  assert(labelling.labels[0] == SIZE_MAX);
  ad_lift_labelling_destroy(&labelling);
  ad_lift_tree_destroy(hosts);
  ADLiftOptions options = {.mode = AD_LIFT_HOST_ADAPTIVE, .symmetric = true};
  assert(!ad_lift_solve(&game, &domain, &options, &result, nullptr, &error));
  options.mode = AD_LIFT_HOST_FULL;
  options.max_host_leaves = 0;
  ADLiftSolveStats stats = {0};
  assert(!ad_lift_solve(&game, &domain, &options, &result, &stats, &error));
  assert(stats.budget_exhausted);
  pg_set_destroy(&domain);
  pg_game_destroy(&game);
}

int main(void) {
  invalid_inputs();
  higher_side_entry();
  random_games();
  family("tests/games/thesis_h4.pg", 50, 23);
  family("tests/games/thesis_h8.pg", 898, 83);
  family("tests/games/thesis_f4.pg", 28, 24);
  family("tests/games/thesis_f8.pg", 241, 112);
  return 0;
}
