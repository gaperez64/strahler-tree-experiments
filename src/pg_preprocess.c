#include <assert.h>
#include <stdlib.h>
#include <string.h>

#include "pg_preprocess.h"

bool pg_preprocess_parse_option(PGPreprocessOptions *options, char const *name,
                                char const *value) {
  if (options == nullptr || name == nullptr) {
    return false;
  }
  if (strcmp(name, "compress") == 0 && value == nullptr) {
    options->compress = true;
    return true;
  }
  if (strcmp(name, "shave") != 0 || value == nullptr) {
    return false;
  }
  unsigned rules = 0;
  if (strcmp(value, "all") == 0) {
    rules = PG_SHAVE_ALL;
  } else if (strcmp(value, "none") != 0) {
    char const *item = value;
    do {
      size_t const length = strcspn(item, ",");
      if (length == 6 && strncmp(item, "single", length) == 0) {
        rules |= 1U << PG_SHAVE_SINGLE;
      } else if (length == 5 && strncmp(item, "loops", length) == 0) {
        rules |= 1U << PG_SHAVE_LOOPS;
      } else if (length == 4 && strncmp(item, "wcwc", length) == 0) {
        rules |= 1U << PG_SHAVE_WCWC;
      } else {
        return false;
      }
      item += length;
      if (*item == '\0') {
        break;
      }
      item++;
    } while (true);
  }
  options->shave = rules;
  return true;
}

void pg_preprocess_destroy(PGPreprocessResult *result) {
  if (result == nullptr) {
    return;
  }
  pg_set_destroy(&result->active);
  for (size_t player = 0; player < 2; player++) {
    pg_set_destroy(&result->won[player]);
  }
  pg_priority_map_destroy(&result->priority_map);
  *result = (PGPreprocessResult){0};
}

[[nodiscard]] static bool remove_dominion(PGGame const *game,
                                          PGPreprocessResult *result,
                                          PGSet const *target,
                                          PGPlayer const player,
                                          PGShaveRule const rule) {
  PGSet attracted = {0};
  if (!pg_attractor(game, &result->active, target, player, &attracted)) {
    return false;
  }
  result->shaved[rule][player] += pg_set_count(&attracted);
  pg_set_union_into(&result->won[player], &attracted);
  pg_set_subtract_into(&result->active, &attracted);
  pg_set_destroy(&attracted);
  return true;
}

[[nodiscard]] static bool shave_single(PGGame const *game,
                                       PGPreprocessResult *result) {
  size_t const first = pg_set_next(&result->active, 0);
  if (first == SIZE_MAX) {
    return true;
  }
  PGPlayer const player = (PGPlayer)(game->vertices[first].priority % 2);
  for (size_t vertex = first; vertex != SIZE_MAX;
       vertex = pg_set_next(&result->active, vertex + 1)) {
    if (game->vertices[vertex].priority % 2 != player) {
      return true;
    }
  }
  return remove_dominion(game, result, &result->active, player,
                         PG_SHAVE_SINGLE);
}

[[nodiscard]] static bool shave_loops(PGGame const *game,
                                      PGPreprocessResult *result,
                                      PGSet target[static 2]) {
  for (size_t player = 0; player < 2; player++) {
    pg_set_clear(&target[player]);
  }
  for (size_t vertex = pg_set_next(&result->active, 0); vertex != SIZE_MAX;
       vertex = pg_set_next(&result->active, vertex + 1)) {
    bool loop = false;
    bool escape = false;
    for (size_t edge = game->succ_offsets[vertex];
         edge < game->succ_offsets[vertex + 1]; edge++) {
      size_t const to = game->successors[edge];
      loop |= to == vertex;
      escape |= to != vertex && pg_set_contains(&result->active, to);
    }
    PGPlayer const player = (PGPlayer)(game->vertices[vertex].priority % 2);
    if (loop && (game->vertices[vertex].owner == player || !escape)) {
      pg_set_add(&target[player], vertex);
    }
  }
  for (size_t player = 0; player < 2; player++) {
    if (!pg_set_empty(&target[player]) &&
        !remove_dominion(game, result, &target[player], (PGPlayer)player,
                         PG_SHAVE_LOOPS)) {
      return false;
    }
  }
  return true;
}

typedef struct {
  uint64_t priority;
  size_t vertex;
} CycleRoot;

typedef struct {
  uint64_t priority;
  size_t index;
  size_t low;
  size_t edge;
} CycleVisit;

static int compare_cycle_roots(void const *left, void const *right) {
  CycleRoot const *a = left;
  CycleRoot const *b = right;
  return (a->priority < b->priority) - (a->priority > b->priority);
}

[[nodiscard]] static bool shave_cycles(PGGame const *game,
                                       PGPreprocessResult *result,
                                       PGSet target[static 2]) {
  if (pg_set_empty(&result->active)) {
    return true;
  }
  size_t const count = game->vertex_count;
  if (count > SIZE_MAX / sizeof(CycleVisit) ||
      count > SIZE_MAX / sizeof(CycleRoot) ||
      count > SIZE_MAX / sizeof(size_t)) {
    return false;
  }
  CycleRoot *roots = malloc(count * sizeof(roots[0]));
  CycleVisit *visits = calloc(count, sizeof(visits[0]));
  size_t *dfs = malloc(count * sizeof(dfs[0]));
  size_t *members = malloc(count * sizeof(members[0]));
  bool succeeded = false;
  if (roots == nullptr || visits == nullptr || dfs == nullptr ||
      members == nullptr) {
    goto cleanup;
  }
  for (size_t player = 0; player < 2; player++) {
    pg_set_clear(&target[player]);
  }
  size_t root_count = 0;
  for (size_t vertex = pg_set_next(&result->active, 0); vertex != SIZE_MAX;
       vertex = pg_set_next(&result->active, vertex + 1)) {
    uint64_t const priority = game->vertices[vertex].priority;
    if (game->vertices[vertex].owner == priority % 2) {
      roots[root_count++] = (CycleRoot){priority, vertex};
    }
  }
  qsort(roots, root_count, sizeof(roots[0]), compare_cycle_roots);

  /* Like oink's solveTrivialCycles, search owner-controlled SCCs from high
   * priorities down, sharing visits at each bound. Lower bounds expose
   * winning cycles hidden by a losing maximum. */
  for (size_t root = 0; root < root_count; root++) {
    uint64_t const priority = roots[root].priority;
    PGPlayer const player = (PGPlayer)(priority % 2);
    size_t const start = roots[root].vertex;
    if (pg_set_contains(&target[player], start) ||
        (visits[start].index != 0 && visits[start].priority == priority)) {
      continue;
    }
    size_t depth = 0;
    size_t member_count = 0;
    size_t index = 0;
    dfs[depth++] = start;
    while (depth != 0) {
      size_t const vertex = dfs[depth - 1];
      CycleVisit *visit = &visits[vertex];
      if (visit->index == 0 || visit->priority != priority) {
        index++;
        *visit =
            (CycleVisit){priority, index, index, game->succ_offsets[vertex]};
        members[member_count++] = vertex;
      }
      bool pushed = false;
      while (visit->edge < game->succ_offsets[vertex + 1]) {
        size_t const to = game->successors[visit->edge++];
        if (!pg_set_contains(&result->active, to) ||
            game->vertices[to].owner != player ||
            game->vertices[to].priority > priority ||
            pg_set_contains(&target[player], to)) {
          continue;
        }
        if (visits[to].index == 0 || visits[to].priority != priority) {
          dfs[depth++] = to;
          pushed = true;
          break;
        }
        if (visits[to].low != SIZE_MAX && visits[to].index < visit->low) {
          visit->low = visits[to].index;
        }
      }
      if (pushed) {
        continue;
      }
      if (visit->low == visit->index) {
        size_t begin = member_count;
        uint64_t maximum = 0;
        do {
          assert(begin != 0);
          size_t const member = members[--begin];
          if (game->vertices[member].priority > maximum) {
            maximum = game->vertices[member].priority;
          }
          visits[member].low = SIZE_MAX;
        } while (members[begin] != vertex);
        bool cycle = member_count - begin > 1;
        for (size_t edge = game->succ_offsets[vertex];
             !cycle && edge < game->succ_offsets[vertex + 1]; edge++) {
          cycle = game->successors[edge] == vertex;
        }
        if (cycle && maximum % 2 == player) {
          for (size_t member = begin; member < member_count; member++) {
            pg_set_add(&target[player], members[member]);
          }
        }
        member_count = begin;
      }
      depth--;
      if (depth != 0 && visit->low < visits[dfs[depth - 1]].low) {
        visits[dfs[depth - 1]].low = visit->low;
      }
    }
  }
  for (size_t player = 0; player < 2; player++) {
    if (!pg_set_empty(&target[player]) &&
        !remove_dominion(game, result, &target[player], (PGPlayer)player,
                         PG_SHAVE_WCWC)) {
      goto cleanup;
    }
  }
  succeeded = true;
cleanup:
  free(roots);
  free(visits);
  free(dfs);
  free(members);
  return succeeded;
}

bool pg_preprocess(PGGame *game, PGPreprocessOptions const *options,
                   PGPreprocessResult *result) {
  if (game == nullptr || options == nullptr || result == nullptr ||
      (options->shave & ~PG_SHAVE_ALL) != 0) {
    return false;
  }
  *result = (PGPreprocessResult){0};
  PGSet target[2] = {0};
  if (!pg_priority_map_build(game, &result->priority_map) ||
      !pg_set_init(&result->active, game->vertex_count) ||
      !pg_set_init(&result->won[PG_EVEN], game->vertex_count) ||
      !pg_set_init(&result->won[PG_ODD], game->vertex_count) ||
      !pg_set_init(&target[0], game->vertex_count) ||
      !pg_set_init(&target[1], game->vertex_count)) {
    goto failure;
  }
  pg_set_fill(&result->active);
  if (!pg_subgame_is_total(game, &result->active)) {
    goto failure;
  }
  if (options->compress) {
    PGPriorityMap *map = &result->priority_map;
    for (size_t index = 1; index < map->count; index++) {
      map->entries[index].compact = map->entries[index - 1].compact +
                                    (map->entries[index].original % 2 !=
                                     map->entries[index - 1].original % 2);
    }
  }
  /* Shaving only uses priority order and parity, so delay mutation until all
   * allocation-dependent work succeeds. */
  size_t before = 0;
  do {
    before = pg_set_count(&result->active);
    if (((options->shave & (1U << PG_SHAVE_SINGLE)) != 0 &&
         !shave_single(game, result)) ||
        ((options->shave & (1U << PG_SHAVE_LOOPS)) != 0 &&
         !shave_loops(game, result, target)) ||
        ((options->shave & (1U << PG_SHAVE_WCWC)) != 0 &&
         !shave_cycles(game, result, target))) {
      goto failure;
    }
  } while (pg_set_count(&result->active) != before);
  if (!pg_priority_map_apply(&result->priority_map, game)) {
    goto failure;
  }
  pg_set_destroy(&target[0]);
  pg_set_destroy(&target[1]);
  return true;

failure:
  pg_set_destroy(&target[0]);
  pg_set_destroy(&target[1]);
  pg_preprocess_destroy(result);
  return false;
}

bool pg_preprocess_verify(PGGame const *game,
                          PGPreprocessResult const *result) {
  if (game == nullptr || result == nullptr ||
      result->active.bit_count != game->vertex_count ||
      result->won[0].bit_count != game->vertex_count ||
      result->won[1].bit_count != game->vertex_count ||
      !pg_subgame_is_total(game, &result->active)) {
    return false;
  }
  PGSet full = {0};
  PGSet complement = {0};
  PGSet attracted = {0};
  bool verified = false;
  if (!pg_set_init(&full, game->vertex_count) ||
      !pg_set_init(&complement, game->vertex_count)) {
    goto cleanup;
  }
  pg_set_fill(&full);
  if (pg_set_count(&result->active) + pg_set_count(&result->won[0]) +
          pg_set_count(&result->won[1]) !=
      game->vertex_count) {
    goto cleanup;
  }
  pg_set_union_into(&complement, &result->active);
  pg_set_union_into(&complement, &result->won[0]);
  pg_set_union_into(&complement, &result->won[1]);
  if (!pg_set_equal(&complement, &full)) {
    goto cleanup;
  }
  for (size_t player = 0; player < 2; player++) {
    pg_set_fill(&complement);
    pg_set_subtract_into(&complement, &result->won[player]);
    if (!pg_attractor(game, &full, &result->won[player], (PGPlayer)player,
                      &attracted) ||
        !pg_set_equal(&attracted, &result->won[player]) ||
        !pg_attractor(game, &full, &complement, (PGPlayer)(1 - player),
                      &attracted) ||
        !pg_set_equal(&attracted, &complement)) {
      goto cleanup;
    }
  }
  verified = true;
cleanup:
  pg_set_destroy(&full);
  pg_set_destroy(&complement);
  pg_set_destroy(&attracted);
  return verified;
}
