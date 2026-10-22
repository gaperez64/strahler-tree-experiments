#ifndef AD_TREE_JSON_H
#define AD_TREE_JSON_H 1

#include "ad_tree_dot.h"
#include "json_utils.h"

/* The result fragment is shared verbatim with trace result/phase events. */
[[nodiscard]] bool ad_json_result(JSONWriter const *writer,
                                  ADResult const *value, ADDotPlayer player);
[[nodiscard]] bool ad_json_result_fields(JSONWriter const *writer,
                                         ADResult const *value,
                                         ADDotPlayer selected);
[[nodiscard]] bool ad_json_metrics(FILE *stream, ADResult const *value,
                                   ADDotPlayer player);

#endif
