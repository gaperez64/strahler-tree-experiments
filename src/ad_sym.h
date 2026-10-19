#ifndef AD_SYM_H
#define AD_SYM_H 1

#include "ad_lift.h"

typedef struct {
  size_t calls;
  /* Calls containing a vertex in the higher player's side fibre at entry. */
  size_t higher_side_calls;
  size_t attractors;
  size_t moves;
  size_t sets;
  size_t certification_lifts;
  size_t separator;
} ADSymStats;

/* Thesis Algorithms 8/9. nullptr hosts selects Algorithm 8's implicit complete
 * n-ary trees; otherwise hosts[p] is player p's tree for Algorithm 9.
 * Restricted hosts yield certified dominions and an unresolved remainder,
 * rather than attributing the whole Theorem F separator to its player. */
[[nodiscard]]
bool ad_sym_solve(PGGame const *game, PGSet const *domain,
                  ADLiftTree const *hosts, bool verify, ADResult *result,
                  ADSymStats *stats, ADLiftError *error);

#endif
