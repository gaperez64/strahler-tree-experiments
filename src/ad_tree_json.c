#include <inttypes.h>
#include <stdlib.h>

#include "ad_tree_json.h"

static void relative_set(JSONWriter const *writer, PGSet const *outer,
                         PGSet const *core, ADNode const *root,
                         char const part) {
  FILE *stream = writer->stream;
  fputc('[', stream);
  bool first = true;
  for (size_t vertex = pg_set_next(outer, 0); vertex != SIZE_MAX;
       vertex = pg_set_next(outer, vertex + 1)) {
    bool const highest =
        pg_set_contains(core, vertex) &&
        writer->game->vertices[vertex].priority == root->priority_bound;
    bool const included =
        part == 'H' ? highest
        : part == 'T'
            ? pg_set_contains(&root->top_attractor, vertex) && !highest
            : !pg_set_contains(core, vertex);
    if (included) {
      fprintf(stream, "%s%" PRIu64, first ? "" : ",",
              writer->game->vertices[vertex].external_id);
      first = false;
    }
  }
  fputc(']', stream);
}

bool ad_json_tree(JSONWriter const *writer, PGSet const *outer,
                  PGSet const *core, ADNode const *root) {
  FILE *stream = writer->stream;
  if (root == nullptr) {
    fputs("null", stream);
    return true;
  }
  fprintf(stream, "{\"h\":%" PRIu64 ",\"H\":", root->priority_bound);
  relative_set(writer, outer, core, root, 'H');
  fputs(",\"T\":", stream);
  relative_set(writer, outer, core, root, 'T');
  fputs(",\"S\":", stream);
  relative_set(writer, outer, core, root, 'S');
  fputs(",\"children\":[", stream);
  for (size_t index = 0; index < root->child_count; index++) {
    ADChild const *child = root->children + index;
    if (index != 0) {
      fputc(',', stream);
    }
    if (!ad_json_tree(writer, &child->attractor, &child->trap,
                      child->subtree)) {
      return false;
    }
  }
  fputs("]}", stream);
  return true;
}

bool ad_json_result_fields(JSONWriter const *writer, ADResult const *value,
                           ADDotPlayer const selected) {
  FILE *stream = writer->stream;
  fprintf(stream, "\"complete\":%s,\"regions\":[",
          value->kind == AD_RESULT_COMPLETE ? "true" : "false");
  json_set(writer, value->region);
  fputc(',', stream);
  json_set(writer, value->region + 1);
  fputs("],\"unresolved\":", stream);
  json_set(writer, &value->unresolved);
  fputs(",\"trees\":[", stream);
  for (size_t player = 0; player < 2; player++) {
    if (player != 0) {
      fputc(',', stream);
    }
    if (!ad_json_tree(
            writer, value->region + player, value->region + player,
            (selected == AD_DOT_PLAYER_EVEN && player != PG_EVEN) ||
                    (selected == AD_DOT_PLAYER_ODD && player != PG_ODD)
                ? nullptr
                : value->decomposition[player])) {
      return false;
    }
  }
  fputs("],\"shaves\":[", stream);
  for (size_t index = 0; index < value->shave_count; index++) {
    if (index != 0) {
      fputc(',', stream);
    }
    fputs("{\"certified\":", stream);
    if (!ad_json_result(writer, &value->shaves[index].certified, selected)) {
      return false;
    }
    fputs(",\"attracted\":[", stream);
    json_set(writer, value->shaves[index].attracted);
    fputc(',', stream);
    json_set(writer, value->shaves[index].attracted + 1);
    fputs("]}", stream);
  }
  fputc(']', stream);
  return !ferror(stream);
}

bool ad_json_result(JSONWriter const *writer, ADResult const *value,
                    ADDotPlayer const player) {
  fputc('{', writer->stream);
  return ad_json_result_fields(writer, value, player) &&
         fputc('}', writer->stream) != EOF;
}

typedef struct {
  size_t *widths;
  size_t max_arity;
  size_t branching_nodes;
  size_t min_leaf_depth;
  size_t leaf_depth_sum;
} ShapeMetrics;

static void shape_metrics(ADNode const *node, size_t const depth,
                          ShapeMetrics *metrics) {
  if (node == nullptr) {
    return;
  }
  metrics->widths[depth - 1]++;
  if (node->child_count > metrics->max_arity) {
    metrics->max_arity = node->child_count;
  }
  metrics->branching_nodes += node->child_count >= 2;
  if (node->child_count == 0) {
    if (metrics->min_leaf_depth == 0 || depth < metrics->min_leaf_depth) {
      metrics->min_leaf_depth = depth;
    }
    metrics->leaf_depth_sum += depth;
  }
  for (size_t index = 0; index < node->child_count; index++) {
    shape_metrics(node->children[index].subtree, depth + 1, metrics);
  }
}

static bool metrics(FILE *stream, ADNode const *root) {
  ADTreeMetrics const base = ad_tree_metrics(root);
  ShapeMetrics shape = {0};
  size_t width = 0;
  if (base.height != 0) {
    shape.widths = calloc(base.height, sizeof(shape.widths[0]));
    if (shape.widths == nullptr) {
      return false;
    }
    shape_metrics(root, 1, &shape);
    for (size_t depth = 0; depth < base.height; depth++) {
      if (shape.widths[depth] > width) {
        width = shape.widths[depth];
      }
    }
    free(shape.widths);
  }
  size_t const internal = base.nodes - base.leaves;
  return fprintf(stream,
                 "{\"nodes\":%zu,\"leaves\":%zu,\"internal_nodes\":%zu,"
                 "\"height\":%zu,\"width\":%zu,\"max_arity\":%zu,"
                 "\"mean_internal_arity\":%.3f,\"branching_nodes\":%zu,"
                 "\"min_leaf_depth\":%zu,\"mean_leaf_depth\":%.3f,\"strahler\":"
                 "%zu}",
                 base.nodes, base.leaves, internal, base.height, width,
                 shape.max_arity,
                 internal == 0 ? 0.0
                               : (double)(base.nodes - 1) / (double)internal,
                 shape.branching_nodes, shape.min_leaf_depth,
                 base.leaves == 0
                     ? 0.0
                     : (double)shape.leaf_depth_sum / (double)base.leaves,
                 base.strahler) >= 0;
}

bool ad_json_metrics(FILE *stream, ADResult const *value,
                     ADDotPlayer const player) {
  fputs("{\"trees\":[", stream);
  for (size_t candidate = 0; candidate < 2; candidate++) {
    if (candidate != 0) {
      fputc(',', stream);
    }
    if ((player == AD_DOT_PLAYER_EVEN && candidate != PG_EVEN) ||
        (player == AD_DOT_PLAYER_ODD && candidate != PG_ODD)) {
      fputs("null", stream);
    } else if (!metrics(stream, value->decomposition[candidate])) {
      return false;
    }
  }
  fputs("],\"shaves\":[", stream);
  for (size_t index = 0; index < value->shave_count; index++) {
    if (index != 0) {
      fputc(',', stream);
    }
    if (!ad_json_metrics(stream, &value->shaves[index].certified, player)) {
      return false;
    }
  }
  return fputs("]}", stream) >= 0 && !ferror(stream);
}
