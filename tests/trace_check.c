#include <assert.h>
#include <errno.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ad_tree.h"
#include "pg_preprocess.h"

static bool read_number(uint64_t *value) {
  char token[32];
  if (scanf("%31s", token) != 1) {
    return false;
  }
  assert(strspn(token, "0123456789") == strlen(token));
  errno = 0;
  char *end = nullptr;
  uintmax_t const number = strtoumax(token, &end, 10);
  assert(errno == 0 && *end == '\0' && number <= UINT64_MAX);
  *value = (uint64_t)number;
  return true;
}

static size_t read_size(void) {
  uint64_t value = 0;
  assert(read_number(&value) && value <= SIZE_MAX);
  return (size_t)value;
}

static int compare_id(void const *key, void const *entry) {
  uint64_t const id = *(uint64_t const *)key;
  PGVertex const *vertex = entry;
  return id < vertex->external_id ? -1 : id > vertex->external_id ? 1 : 0;
}

static PGSet read_set(PGGame const *game) {
  PGSet result = {0};
  assert(pg_set_init(&result, game->vertex_count));
  size_t const count = read_size();
  for (size_t index = 0; index < count; index++) {
    uint64_t id = 0;
    assert(read_number(&id));
    PGVertex const *vertex = bsearch(&id, game->vertices, game->vertex_count,
                                     sizeof(game->vertices[0]), compare_id);
    assert(vertex != nullptr);
    pg_set_add(&result, (size_t)(vertex - game->vertices));
  }
  return result;
}

static ADNode *read_node(PGGame const *game, PGPlayer const player) {
  size_t const present = read_size();
  assert(present <= 1);
  if (present == 0) {
    return nullptr;
  }
  uint64_t bound = 0;
  assert(read_number(&bound));
  ADNode *node = ad_node_create(player, bound, game->vertex_count);
  assert(node != nullptr);
  PGSet top = read_set(game);
  pg_set_move(&node->top_attractor, &top);
  size_t const count = read_size();
  for (size_t index = 0; index < count; index++) {
    ADChild child = {0};
    child.trap = read_set(game);
    child.attractor = read_set(game);
    child.subtree = read_node(game, player);
    assert(ad_node_append_child(node, &child));
  }
  return node;
}

int main(int argc, char *argv[]) {
  assert(argc == 3);
  FILE *stream = fopen(argv[1], "r");
  assert(stream != nullptr);
  PGGame game = {0};
  PGParseError error = {0};
  assert(pg_game_read(stream, &game, &error));
  assert(fclose(stream) == 0);
  PGPreprocessOptions options = {.compress = argv[2][0] == '1'};
  PGPreprocessResult pre = {0};
  assert(pg_preprocess(&game, &options, &pre));
  uint64_t player = 0;
  while (read_number(&player)) {
    assert(player <= PG_ODD);
    PGSet domain = read_set(&game);
    ADNode *node = read_node(&game, (PGPlayer)player);
    ADVerifyError verification = {0};
    bool const valid =
        ad_tree_check(&game, &domain, (PGPlayer)player, node, &verification);
    printf("%d %d\n", (int)valid, (int)verification.condition);
    ad_node_destroy(node);
    pg_set_destroy(&domain);
  }
  pg_preprocess_destroy(&pre);
  pg_game_destroy(&game);
  return 0;
}
