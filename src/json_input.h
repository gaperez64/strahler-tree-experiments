#ifndef JSON_INPUT_H
#define JSON_INPUT_H 1

#include <stdint.h>

typedef enum { J_NULL, J_NUMBER, J_STRING, J_ARRAY, J_OBJECT } JSONKind;
typedef struct JSONValue JSONValue;
struct JSONValue {
  JSONKind kind;
  uint64_t number;
  char *string;
  char *key;
  JSONValue *child;
  JSONValue *next;
};

/* Strict JSON for the API's integer/ASCII tree and label input vocabulary.
 * Nesting is bounded; duplicate object keys are rejected. */
JSONValue *json_parse_input(char const *text);
void json_input_destroy(JSONValue *value);
JSONValue const *json_member(JSONValue const *object, char const *key);

#endif
