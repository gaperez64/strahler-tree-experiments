#ifndef PM_TREE_DOT_H
#define PM_TREE_DOT_H 1

#include "ad_tree_dot.h"
#include "pm_lift.h"

[[nodiscard]] bool pm_write_leaves(FILE *out, PMResult const *result);
[[nodiscard]] bool
pm_write_dot(FILE *out, PGGame const *game, PMResult const result[static 2],
             PGSet const *unresolved, size_t round, bool incremental,
             ADDotPlayer player, ADDotLabels labels, size_t max_set_items,
             PGPriorityMap const *priority_map, PGSet const shaved[static 2]);

[[nodiscard]] bool
pm_write_json(FILE *out, PGGame const *game, PMResult const result[static 2],
              PGSet const *unresolved, size_t round, ADDotPlayer player,
              PGPriorityMap const *priority_map, PGSet const shaved[static 2]);

#endif
