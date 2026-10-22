#ifndef STRAHLER_H
#define STRAHLER_H 1

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(__GNUC__)
#define STRAHLER_API __attribute__((visibility("default")))
#else
#define STRAHLER_API
#endif

typedef struct strahler_game strahler_game;
typedef int (*strahler_event_cb)(void *context, char const *line,
                                 size_t length);

/* All returned strings belong to the caller; release with strahler_free.
 * Outputs are cleared on entry. Error messages can be NULL on allocation
 * failure. Status: 0 success, 1 observer/runtime, 2 argument, 3 game,
 * 4 solver/verification, 5 I/O, 6 allocation. No process-global state is used.
 * Games are immutable and may be shared by concurrent calls. Callbacks run
 * synchronously, borrow a JSON line, and return nonzero to continue. */
STRAHLER_API int strahler_game_parse(char const *text, size_t length,
                                     strahler_game **game, char **error);
STRAHLER_API void strahler_game_free(strahler_game *game);
STRAHLER_API int strahler_game_summary(strahler_game const *game, char **json,
                                       char **error);
/* argv contains only --name[=value] CLI options, without a program name,
 * filename, output format or trace file. JSON output is implicit. */
STRAHLER_API int strahler_decompose(strahler_game const *game,
                                    char const *const argv[], int argc,
                                    strahler_event_cb callback, void *context,
                                    char **json, char **error);
STRAHLER_API int strahler_progress_measures(strahler_game const *game,
                                            char const *const argv[], int argc,
                                            char **json, char **error);
/* tree_json: null or {h,H,T,S,children}; subgame_json: vertex ID array,
 * NULL selects the whole game. Check failure is a successful API call with
 * ok=false; malformed input and allocation failure are API errors. Bounds
 * use solver normalization; compress (0/1) must match the producing run. */
STRAHLER_API int strahler_check(strahler_game const *game,
                                char const *tree_json, int player,
                                char const *subgame_json, int compress,
                                char **json, char **error);
/* labels_json: {player,h,tree,labels}; tree is a pms2dot leaf stream,
 * labels is an array of {vertex,path,part}, part in H/T/S (root S = TOP).
 * Returns {tree,problems}; see docs/developing.md for this input format. */
STRAHLER_API int strahler_materialize_partial(strahler_game const *game,
                                              char const *labels_json,
                                              int compress, char **json,
                                              char **error);
STRAHLER_API int strahler_genstree(int k, int h, int t, char **json,
                                   char **error);
/* Leaf paths are limited to 1025 components before recursive tree operations.
 */
STRAHLER_API int strahler_pms_tree(char const *text, size_t length,
                                   char const *const argv[], int argc,
                                   char **json, char **error);
STRAHLER_API void strahler_free(void *value);
/* ABI compatibility is guaranteed within the 0.3.x release series only. */
STRAHLER_API char const *strahler_version(void);

#ifdef __cplusplus
}
#endif

#endif
