#include <assert.h>
#include <stdlib.h>
#include <string.h>

#include "ad_lift_solve.h"
#include "zielonka.h"

static bool seen[AD_VERIFY_EMPTY_CORE + 1];

static void located(ADVerifyError const *error, ADVerifyCondition const code,
                    size_t const vertex, bool const child) {
  assert(error->condition == code);
  assert(error->vertex == vertex);
  assert(error->path_length == (child ? 1 : 0));
  assert(!child || error->path[0] == 0);
  assert(error->message[0] != '\0');
  seen[code] = true;
}

static PGGame read_game(char const *text) {
  FILE *stream = tmpfile();
  assert(stream != nullptr);
  assert(fputs(text, stream) >= 0);
  assert(fseek(stream, 0, SEEK_SET) == 0);
  PGGame game = {0};
  PGParseError error = {0};
  assert(pg_game_read(stream, &game, &error));
  assert(fclose(stream) == 0);
  return game;
}

static void trees(void) {
  PGGame game = read_game("0 2 0 0;1 0 0 1;2 0 0 2;3 1 1 3;");
  PGSet domain = {0};
  assert(pg_set_init(&domain, game.vertex_count));
  pg_set_fill(&domain);
  ADResult result = {0};
  ZielonkaError error = {0};
  assert(zielonka_decompose(&game, &domain, 2, &result, &error));
  ADNode *root = result.decomposition[0];
  assert(root->child_count == 1);
  ADChild *child = root->children;
  ADVerifyError verification = {0};
  assert(ad_tree_check(&game, result.region, PG_EVEN, root, &verification));
  PGSet subgame = {0};
  assert(pg_set_init(&subgame, game.vertex_count));
  pg_set_add(&subgame, 1);
  assert(ad_tree_check(&game, &subgame, PG_EVEN, root, &verification));
  assert(pg_set_contains(&root->top_attractor, 0) &&
         pg_set_contains(&child->trap, 2));
  pg_set_clear(&subgame);
  assert(ad_tree_check(&game, &subgame, PG_EVEN, root, &verification));
  pg_set_add(&subgame, 2);
  pg_set_remove(&child->trap, 2);
  pg_set_remove(&child->attractor, 2);
  pg_set_remove(&child->subtree->top_attractor, 2);
  ADChild broken = {.subtree = ad_node_create(PG_EVEN, 0, game.vertex_count)};
  assert(broken.subtree != nullptr);
  assert(pg_set_init(&broken.trap, game.vertex_count));
  assert(pg_set_init(&broken.attractor, game.vertex_count));
  pg_set_add(&broken.trap, 2);
  pg_set_add(&broken.attractor, 2);
  assert(ad_node_append_child(root, &broken));
  child = root->children;
  assert(!ad_tree_check(&game, &subgame, PG_EVEN, root, &verification));
  assert(verification.condition == AD_VERIFY_TOP && verification.vertex == 2 &&
         verification.path_length == 1 && verification.path[0] == 1);
  pg_set_destroy(&root->children[1].trap);
  pg_set_destroy(&root->children[1].attractor);
  ad_node_destroy(root->children[1].subtree);
  root->children[1] = (ADChild){0};
  root->child_count = 1;
  pg_set_add(&child->trap, 2);
  pg_set_add(&child->attractor, 2);
  pg_set_add(&child->subtree->top_attractor, 2);
  pg_set_destroy(&subgame);
  assert(!ad_tree_verify(nullptr, result.region, root, &verification));
  located(&verification, AD_VERIFY_INPUT, SIZE_MAX, false);
  root->player = PG_ODD;
  assert(!ad_tree_verify(&game, result.region, root, &verification));
  located(&verification, AD_VERIFY_NODE, SIZE_MAX, false);
  assert(!ad_result_verify_partial(&game, &domain, &result, &verification));
  located(&verification, AD_VERIFY_NODE, SIZE_MAX, false);
  root->player = PG_EVEN;
  root->priority_bound = 0;
  assert(!ad_tree_verify(&game, result.region, root, &verification));
  located(&verification, AD_VERIFY_PRIORITY, 0, false);
  root->priority_bound = 2;
  pg_set_remove(&root->top_attractor, 0);
  assert(!ad_tree_verify(&game, result.region, root, &verification));
  located(&verification, AD_VERIFY_TOP, 0, false);
  pg_set_add(&root->top_attractor, 0);
  PGSet saved_top = {0};
  assert(pg_set_clone(&saved_top, &root->top_attractor));
  assert(pg_set_clone(&root->top_attractor, result.region));
  root->priority_bound = game.vertices[0].priority = 0;
  assert(!ad_tree_verify(&game, result.region, root, &verification));
  located(&verification, AD_VERIFY_CHILD_BOUND, SIZE_MAX, false);
  pg_set_move(&root->top_attractor, &saved_top);
  root->priority_bound = game.vertices[0].priority = 2;
  pg_set_add(&child->trap, 0);
  assert(!ad_tree_verify(&game, result.region, root, &verification));
  located(&verification, AD_VERIFY_TRAP, 0, true);
  pg_set_remove(&child->trap, 0);
  child->subtree->priority_bound = 1;
  assert(!ad_tree_verify(&game, result.region, root, &verification));
  located(&verification, AD_VERIFY_CHILD, SIZE_MAX, true);
  child->subtree->priority_bound = 0;
  pg_set_remove(&child->attractor, 1);
  assert(!ad_tree_verify(&game, result.region, root, &verification));
  located(&verification, AD_VERIFY_ATTRACTOR, 1, true);
  pg_set_add(&child->attractor, 1);
  root->child_count = 0;
  assert(!ad_tree_verify(&game, result.region, root, &verification));
  located(&verification, AD_VERIFY_PARTITION, 1, false);
  root->child_count = 1;
  pg_set_remove(&child->trap, 2);
  pg_set_remove(&child->subtree->top_attractor, 2);
  assert(!ad_tree_relative_verify(&game, result.region, root, &verification));
  located(&verification, AD_VERIFY_CORE, 2, true);
  PGGame escaping = read_game("0 2 0 0;1 0 0 2;2 0 0 1;3 1 1 3;");
  assert(
      !ad_tree_relative_verify(&escaping, result.region, root, &verification));
  located(&verification, AD_VERIFY_TRAP, 1, true);
  pg_game_destroy(&escaping);
  pg_set_add(&child->trap, 2);
  pg_set_add(&child->subtree->top_attractor, 2);
  result.decomposition[0] = nullptr;
  assert(!ad_result_verify_complete(&game, &domain, &result, &verification));
  located(&verification, AD_VERIFY_REGION, 0, false);
  result.decomposition[0] = root;
  result.kind = AD_RESULT_PARTIAL;
  assert(!ad_result_verify_complete(&game, &domain, &result, &verification));
  located(&verification, AD_VERIFY_INCOMPLETE, SIZE_MAX, false);
  result.kind = AD_RESULT_COMPLETE;
  pg_set_remove(&domain, 2);
  assert(!ad_result_verify_partial(&game, &domain, &result, &verification));
  located(&verification, AD_VERIFY_PARTITION, 2, false);
  pg_set_add(&domain, 2);
  ADResult incomplete = {.kind = AD_RESULT_COMPLETE};
  assert(pg_set_init(incomplete.region, game.vertex_count));
  assert(pg_set_init(incomplete.region + 1, game.vertex_count));
  assert(pg_set_clone(&incomplete.unresolved, &domain));
  assert(
      !ad_result_verify_complete(&game, &domain, &incomplete, &verification));
  located(&verification, AD_VERIFY_INCOMPLETE, 0, false);
  ad_result_destroy(&incomplete);
  ADShaveRound shave = {.certified = result};
  assert(pg_set_clone(shave.attracted, result.region));
  assert(pg_set_clone(shave.attracted + 1, result.region + 1));
  pg_set_remove(shave.attracted, 0);
  ADResult outer = {.shave_count = 1, .shaves = &shave};
  assert(pg_set_init(outer.region, game.vertex_count));
  assert(pg_set_init(outer.region + 1, game.vertex_count));
  assert(pg_set_init(&outer.unresolved, game.vertex_count));
  assert(!ad_result_verify_partial(&game, &domain, &outer, &verification));
  located(&verification, AD_VERIFY_SHAVE, 0, false);
  outer.shave_count = 0;
  outer.shaves = nullptr;
  ad_result_destroy(&outer);
  pg_set_destroy(shave.attracted);
  pg_set_destroy(shave.attracted + 1);
  ad_result_destroy(&result);
  pg_set_destroy(&domain);
  pg_game_destroy(&game);

  game = read_game("0 0 0 1;1 0 0 1;");
  assert(pg_set_init(&domain, 2));
  pg_set_add(&domain, 0);
  root = ad_node_create(PG_EVEN, 0, 2);
  assert(root != nullptr);
  assert(!ad_tree_check(&game, &domain, PG_EVEN, root, &verification));
  located(&verification, AD_VERIFY_TOTALITY, 0, false);
  ad_node_destroy(root);
  pg_set_destroy(&domain);
  pg_game_destroy(&game);
}

static void labellings(void) {
  PGGame game = read_game("0 2 1 1;1 1 1 1;2 1 1 2;");
  ADLiftTree host = {0};
  ADLiftError error = {0};
  assert(ad_lift_tree_build_full(2, 2, PG_EVEN, 2, &host, &error));
  PGSet active = {0};
  assert(pg_set_init(&active, 3));
  pg_set_fill(&active);
  ADLiftLabelling labels = {.vertex_count = 3};
  labels.labels = malloc(3 * sizeof(size_t));
  assert(labels.labels != nullptr);
  assert(pg_set_init(&labels.dominion, 3));
  for (size_t vertex = 0; vertex < 3; vertex++) {
    labels.labels[vertex] = host.top;
  }
  ADVerifyError verification = {0};
  assert(ad_lift_verify(&game, &active, &host, &labels, &verification));
  pg_set_remove(&active, 2);
  assert(!ad_lift_verify(&game, &active, &host, &labels, &verification));
  located(&verification, AD_VERIFY_INACTIVE, 2, false);
  labels.labels[2] = host.nodes[1].after;
  assert(!ad_lift_verify(&game, &active, &host, &labels, &verification));
  located(&verification, AD_VERIFY_INACTIVE, 2, true);
  labels.labels[2] = SIZE_MAX;
  labels.labels[0] = host.top + 1;
  assert(!ad_lift_verify(&game, &active, &host, &labels, &verification));
  located(&verification, AD_VERIFY_POSITION, 0, false);
  labels.labels[0] = host.nodes[1].regular;
  assert(!ad_lift_verify(&game, &active, &host, &labels, &verification));
  located(&verification, AD_VERIFY_COMPATIBILITY, 0, true);
  labels.labels[0] = host.nodes[0].regular;
  assert(!ad_lift_verify(&game, &active, &host, &labels, &verification));
  located(&verification, AD_VERIFY_DOMINION, 0, false);
  pg_set_add(&labels.dominion, 0);
  assert(!ad_lift_verify(&game, &active, &host, &labels, &verification));
  located(&verification, AD_VERIFY_REGULAR, 0, false);
  labels.labels[0] = host.top;
  pg_set_remove(&labels.dominion, 0);
  labels.labels[1] = host.nodes[0].minus_inf;
  pg_set_add(&labels.dominion, 1);
  assert(!ad_lift_verify(&game, &active, &host, &labels, &verification));
  located(&verification, AD_VERIFY_LAZY, 1, false);
  labels.labels[1] = host.nodes[1].after;
  labels.labels[2] = host.nodes[2].after;
  pg_set_add(&labels.dominion, 2);
  ADNode *candidate = nullptr;
  ADVerifyError *problems = nullptr;
  size_t count = 0;
  assert(!ad_lift_materialize(&game, &host, &labels, &candidate, &error));
  assert(ad_lift_materialize_partial(&game, &host, &labels, &candidate,
                                     &problems, &count, &error));
  assert(candidate != nullptr && candidate->child_count == 2 && count == 2);
  located(problems, AD_VERIFY_EMPTY_CORE, 1, true);
  assert(problems[1].condition == AD_VERIFY_EMPTY_CORE &&
         problems[1].path_length == 1 && problems[1].path[0] == 1 &&
         problems[1].vertex == 2);
  free(problems);
  ad_node_destroy(candidate);
  ad_lift_labelling_destroy(&labels);
  ad_lift_tree_destroy(&host);
  pg_set_destroy(&active);
  pg_game_destroy(&game);
}

static bool reject(void *context, ADTraceEvent const *event) {
  size_t *steps = context;
  ++*steps;
  assert(event->step == *steps);
  return event->step < 4;
}

static void observers(void) {
  PGGame game = read_game("0 2 0 1;1 0 0 1;");
  PGSet active = {0};
  assert(pg_set_init(&active, 2));
  pg_set_fill(&active);
  for (size_t algorithm = 0; algorithm < 4; algorithm++) {
    size_t steps = 0;
    ADTrace trace = {.callback = reject, .context = &steps};
    ADResult result = {0};
    ADLiftError error = {0};
    ZielonkaError zielonka_error = {0};
    bool success = false;
    if (algorithm == 0) {
      success = zielonka_decompose_trace(&game, &active, 2, &result, nullptr,
                                         &zielonka_error, &trace);
    } else if (algorithm == 1) {
      success = ad_sym_solve_trace(&game, &active, nullptr, true, &result,
                                   nullptr, &error, &trace);
    } else {
      ADLiftOptions options = {.mode = AD_LIFT_HOST_FULL,
                               .max_host_leaves = SIZE_MAX,
                               .verify = true,
                               .trace = &trace,
                               .symmetric = algorithm == 3};
      success =
          ad_lift_solve(&game, &active, &options, &result, nullptr, &error);
    }
    assert(!success && trace.failed && steps == 4);
    ad_result_destroy(&result);
  }
  pg_set_destroy(&active);
  pg_game_destroy(&game);
}

int main(void) {
  trees();
  labellings();
  observers();
  /* Allocation failure is covered in test_ad_trace_alloc. */
  for (ADVerifyCondition code = AD_VERIFY_INPUT; code <= AD_VERIFY_EMPTY_CORE;
       code++) {
    assert(code == AD_VERIFY_MEMORY || seen[code]);
  }
  return 0;
}
