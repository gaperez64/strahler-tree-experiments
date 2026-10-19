#ifndef ZIELONKA_H
#define ZIELONKA_H 1

#include <stddef.h>
#include <stdint.h>

#include "ad_tree.h"

typedef struct {
  char message[256];
} ZielonkaError;

typedef struct {
  size_t calls;
  size_t attractors;
} ZielonkaStats;

[[nodiscard]]
bool zielonka_decompose_stats(PGGame const *game, PGSet const *domain,
                              uint64_t bound, ADResult *result,
                              ZielonkaStats *stats, ZielonkaError *error);

[[nodiscard]]
bool zielonka_decompose(PGGame const *game, PGSet const *domain, uint64_t bound,
                        ADResult *result, ZielonkaError *error);

#endif
