#include <inttypes.h>
#include <string.h>

#include "ad_trace.h"

void ad_trace_emit(ADTrace *trace, ADTraceEvent event) {
  if (trace->failed) {
    return;
  }
  event.step = ++trace->step;
  if (trace->callback == nullptr || !trace->callback(trace->context, &event)) {
    trace->failed = true;
  }
}

ADTracePath ad_trace_host_path(ADLiftTree const *host, size_t node,
                               size_t storage[AD_PATH_CAPACITY]) {
  size_t length = 0;
  while (node != 0 && node < host->node_count && length < AD_PATH_CAPACITY) {
    size_t const parent = host->nodes[node].parent;
    size_t index = 0;
    for (size_t sibling = host->nodes[parent].first_child; sibling != node;
         sibling = host->nodes[sibling].next_sibling) {
      index++;
    }
    storage[length++] = index;
    node = parent;
  }
  for (size_t index = 0; index < length / 2; index++) {
    size_t const value = storage[index];
    storage[index] = storage[length - index - 1];
    storage[length - index - 1] = value;
  }
  return (ADTracePath){storage, length};
}

void ad_trace_label(ADTrace *trace, ADLiftTree const *host, size_t const vertex,
                    size_t const node, ADPositionKind const kind,
                    ADTraceKind const event, size_t const from,
                    size_t const to) {
  size_t storage[AD_PATH_CAPACITY];
  ADTracePath const path = ad_trace_host_path(host, node, storage);
  ad_trace_emit(trace, (ADTraceEvent){.kind = event,
                                      .player = host->player,
                                      .path = path,
                                      .h = host->nodes[node].level,
                                      .part = kind == AD_POS_REGULAR     ? 'H'
                                              : kind == AD_POS_MINUS_INF ? 'T'
                                                                         : 'S',
                                      .vertex = vertex,
                                      .from = from,
                                      .to = to});
}

void ad_trace_tree(ADTrace *trace, PGGame const *game, PGSet const *outer,
                   PGSet const *core, ADNode const *root, ADTracePath path) {
  if (root == nullptr || trace->failed) {
    return;
  }
  ADTreeRelativeParts parts = {0};
  if (!ad_tree_relative_parts(game, outer, core, root, &parts)) {
    trace->failed = true;
    return;
  }
  /* An unfinished node has only the H vertices actually stored in its top. */
  pg_set_intersect_into(&parts.highest, &root->top_attractor);
  PGSet const *sets[] = {&parts.highest, &parts.top, &parts.side};
  for (size_t index = 0; index < 3; index++) {
    ad_trace_emit(trace, (ADTraceEvent){.kind = AD_TRACE_SET,
                                        .player = root->player,
                                        .path = path,
                                        .h = root->priority_bound,
                                        .part = "HTS"[index],
                                        .vertices = sets[index],
                                        .children = root->child_count});
  }
  ad_tree_relative_parts_destroy(&parts);
  size_t storage[AD_PATH_CAPACITY];
  if (path.length >= AD_PATH_CAPACITY) {
    trace->failed = true;
    return;
  }
  if (path.length != 0) {
    memcpy(storage, path.indices, path.length * sizeof(storage[0]));
  }
  for (size_t index = 0; index < root->child_count; index++) {
    ADChild const *child = root->children + index;
    storage[path.length] = index;
    ad_trace_tree(trace, game, &child->attractor, &child->trap, child->subtree,
                  (ADTracePath){storage, path.length + 1});
  }
}

static void string(FILE *stream, char const *value) {
  fputc('"', stream);
  for (unsigned char const *next = (unsigned char const *)value; *next != 0;
       next++) {
    if (*next == '"' || *next == '\\') {
      fputc('\\', stream);
      fputc(*next, stream);
    } else if (*next < 32) {
      fprintf(stream, "\\u%04x", (unsigned int)*next);
    } else {
      fputc(*next, stream);
    }
  }
  fputc('"', stream);
}

static void set(ADTraceJSON const *writer, PGSet const *vertices) {
  fputc('[', writer->stream);
  bool first = true;
  if (vertices != nullptr) {
    for (size_t vertex = pg_set_next(vertices, 0); vertex != SIZE_MAX;
         vertex = pg_set_next(vertices, vertex + 1)) {
      fprintf(writer->stream, "%s%" PRIu64, first ? "" : ",",
              writer->game->vertices[vertex].external_id);
      first = false;
    }
  }
  fputc(']', writer->stream);
}

static void path(FILE *stream, ADTracePath const value) {
  fputc('[', stream);
  for (size_t index = 0; index < value.length; index++) {
    fprintf(stream, "%s%zu", index == 0 ? "" : ",", value.indices[index]);
  }
  fputc(']', stream);
}

static void relative_set(ADTraceJSON const *writer, PGSet const *outer,
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

static bool tree(ADTraceJSON const *writer, PGSet const *outer,
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
    if (!tree(writer, &child->attractor, &child->trap, child->subtree)) {
      return false;
    }
  }
  fputs("]}", stream);
  return true;
}

static bool result(ADTraceJSON const *writer, ADResult const *value) {
  FILE *stream = writer->stream;
  fprintf(stream, "{\"complete\":%s,\"regions\":[",
          value->kind == AD_RESULT_COMPLETE ? "true" : "false");
  set(writer, value->region);
  fputc(',', stream);
  set(writer, value->region + 1);
  fputs("],\"unresolved\":", stream);
  set(writer, &value->unresolved);
  fputs(",\"trees\":[", stream);
  for (size_t player = 0; player < 2; player++) {
    if (player != 0) {
      fputc(',', stream);
    }
    if (!tree(writer, value->region + player, value->region + player,
              value->decomposition[player])) {
      return false;
    }
  }
  fputs("],\"shaves\":[", stream);
  for (size_t index = 0; index < value->shave_count; index++) {
    if (index != 0) {
      fputc(',', stream);
    }
    fputs("{\"certified\":", stream);
    if (!result(writer, &value->shaves[index].certified)) {
      return false;
    }
    fputs(",\"attracted\":[", stream);
    set(writer, value->shaves[index].attracted);
    fputc(',', stream);
    set(writer, value->shaves[index].attracted + 1);
    fputs("]}", stream);
  }
  fputs("]}", stream);
  return true;
}

bool ad_trace_json_header(ADTraceJSON *writer, char const *version,
                          char const *algorithm, int const argc,
                          char *const argv[]) {
  FILE *stream = writer->stream;
  fputs("{\"event\":\"header\",\"schema\":\"strahler-trace/1\",\"version\":",
        stream);
  string(stream, version);
  fputs(",\"algorithm\":", stream);
  string(stream, algorithm);
  fputs(",\"options\":[", stream);
  for (int index = 1; index < argc; index++) {
    if (index != 1) {
      fputc(',', stream);
    }
    string(stream, argv[index]);
  }
  fputs("]}\n", stream);
  return !ferror(stream);
}

bool ad_trace_json_incomplete(ADTraceJSON *writer, size_t const step,
                              char const *reason, int const status) {
  fprintf(writer->stream,
          "{\"event\":\"incomplete\",\"step\":%zu,\"reason\":", step);
  string(writer->stream, reason);
  fprintf(writer->stream, ",\"exit_status\":%d}\n", status);
  return !ferror(writer->stream);
}

bool ad_trace_json_event(void *context, ADTraceEvent const *event) {
  ADTraceJSON *writer = context;
  FILE *stream = writer->stream;
  if (event->step > writer->limit) {
    fprintf(stream,
            "{\"event\":\"truncated\",\"step\":%zu,\"limit\":%zu,\"player\":%d,"
            "\"path\":",
            event->step, writer->limit, (int)event->player);
    path(stream, event->path);
    fputs("}\n", stream);
    writer->truncated = true;
    return false;
  }
  static char const *const names[] = {
      "call",   "return", "attractor", "set",   "move",  "check",
      "labels", "lift",   "round_end", "phase", "result"};
  fprintf(stream, "{\"event\":\"%s\",\"step\":%zu,\"player\":%d,\"path\":",
          names[event->kind], event->step, (int)event->player);
  path(stream, event->path);
  switch (event->kind) {
  case AD_TRACE_CALL:
    fprintf(stream, ",\"h\":%" PRIu64 ",\"paths\":[", event->h);
    path(stream, event->paths[0]);
    fputc(',', stream);
    path(stream, event->paths[1]);
    fputs("],\"subgame\":", stream);
    set(writer, event->subgame);
    break;
  case AD_TRACE_RETURN:
    fputs(",\"vertices\":", stream);
    set(writer, event->vertices);
    break;
  case AD_TRACE_ATTRACTOR:
    fputs(",\"kind\":", stream);
    string(stream, event->name);
    fputs(",\"target\":", stream);
    set(writer, event->target);
    fputs(",\"vertices\":", stream);
    set(writer, event->vertices);
    if (event->subgame != nullptr) {
      fputs(",\"subgame\":", stream);
      set(writer, event->subgame);
    }
    if (event->safe != nullptr) {
      fputs(",\"safe\":", stream);
      set(writer, event->safe);
    }
    break;
  case AD_TRACE_SET:
  case AD_TRACE_MOVE:
    fprintf(stream,
            ",\"part\":\"%c\",\"h\":%" PRIu64 ",\"children\":%zu,\"vertices\":",
            event->part, event->h, event->children);
    set(writer, event->vertices);
    if (event->kind == AD_TRACE_MOVE) {
      fputs(",\"to_path\":", stream);
      path(stream, event->other_path);
      fprintf(stream, ",\"to_part\":\"%c\"", event->other_part);
    }
    break;
  case AD_TRACE_CHECK:
    fprintf(stream, ",\"is_attractor_decomposition\":%s,\"subgame\":",
            event->valid ? "true" : "false");
    set(writer, event->subgame);
    fputs(",\"reason\":", stream);
    string(stream, event->name);
    break;
  case AD_TRACE_LABELS:
  case AD_TRACE_LIFT:
    fprintf(stream, ",\"vertex\":%" PRIu64 ",\"part\":\"%c\",\"h\":%" PRIu64,
            writer->game->vertices[event->vertex].external_id, event->part,
            event->h);
    if (event->kind == AD_TRACE_LIFT) {
      fprintf(stream, ",\"from\":%zu,\"to\":%zu", event->from, event->to);
    }
    break;
  case AD_TRACE_PHASE:
    fputs(",\"phase\":", stream);
    string(stream, event->name);
    fprintf(stream, ",\"value\":%zu,\"vertices\":", event->to);
    set(writer, event->vertices);
    if (event->result != nullptr) {
      fputs(",\"result\":", stream);
      if (!result(writer, event->result)) {
        return false;
      }
    }
    break;
  case AD_TRACE_RESULT:
    fputs(",\"initial_won\":[", stream);
    set(writer, writer->initial_won);
    fputc(',', stream);
    set(writer,
        writer->initial_won == nullptr ? nullptr : writer->initial_won + 1);
    fputs("],\"result\":", stream);
    if (!result(writer, event->result)) {
      return false;
    }
    break;
  case AD_TRACE_ROUND_END:
    break;
  }
  fputs("}\n", stream);
  return !ferror(stream);
}
