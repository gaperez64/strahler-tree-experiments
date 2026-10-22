#include <ctype.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>

#include "json_input.h"

static void space(char const **text) {
  while (**text == ' ' || **text == '\t' || **text == '\r' || **text == '\n') {
    ++*text;
  }
}

static int hex(char const ch) {
  if (ch >= '0' && ch <= '9') {
    return ch - '0';
  }
  if (ch >= 'a' && ch <= 'f') {
    return ch - 'a' + 10;
  }
  return ch >= 'A' && ch <= 'F' ? ch - 'A' + 10 : -1;
}

static char *string(char const **text) {
  if (**text != '"') {
    return nullptr;
  }
  ++*text;
  char const *end = *text;
  while (*end != '"') {
    if (*end == '\0') {
      return nullptr;
    }
    if (*end == '\\') {
      if (end[1] == '\0') {
        return nullptr;
      }
      end++;
    }
    end++;
  }
  size_t const capacity = (size_t)(end - *text) + 1;
  char *result = malloc(capacity);
  if (result == nullptr) {
    return nullptr;
  }
  size_t length = 0;
  while (**text != '"') {
    unsigned char ch = (unsigned char)**text;
    if (ch < 32 || ch > 126) {
      free(result);
      return nullptr;
    }
    ++*text;
    if (ch == '\\') {
      ch = (unsigned char)**text;
      if (ch == '\0') {
        free(result);
        return nullptr;
      }
      ++*text;
      char const *escapes = "\"\\/bfnrt";
      char const *found = strchr(escapes, ch);
      if (found != nullptr) {
        ch = (unsigned char)"\"\\/\b\f\n\r\t"[found - escapes];
      } else if (ch == 'u') {
        unsigned code = 0;
        for (size_t i = 0; i < 4; i++) {
          int const digit = hex(**text);
          if (digit < 0) {
            free(result);
            return nullptr;
          }
          code = code * 16 + (unsigned)digit;
          ++*text;
        }
        if (code == 0 || code > 127) {
          free(result);
          return nullptr;
        }
        ch = (unsigned char)code;
      } else {
        free(result);
        return nullptr;
      }
    }
    result[length++] = (char)ch;
  }
  ++*text;
  result[length] = '\0';
  return result;
}

void json_input_destroy(JSONValue *value) {
  while (value != nullptr) {
    JSONValue *next = value->next;
    json_input_destroy(value->child);
    free(value->string);
    free(value->key);
    free(value);
    value = next;
  }
}

JSONValue const *json_member(JSONValue const *object, char const *key) {
  if (object == nullptr || object->kind != J_OBJECT) {
    return nullptr;
  }
  for (JSONValue const *value = object->child; value != nullptr;
       value = value->next) {
    if (strcmp(value->key, key) == 0) {
      return value;
    }
  }
  return nullptr;
}

static JSONValue *parse(char const **text, size_t const depth) {
  if (depth > 1026) {
    return nullptr;
  }
  space(text);
  JSONValue *value = calloc(1, sizeof(*value));
  if (value == nullptr) {
    return nullptr;
  }
  if (**text == '"') {
    value->kind = J_STRING;
    value->string = string(text);
    if (value->string == nullptr) {
      goto invalid;
    }
  } else if (**text == '[' || **text == '{') {
    bool const object = **text == '{';
    value->kind = object ? J_OBJECT : J_ARRAY;
    char const close = object ? '}' : ']';
    ++*text;
    space(text);
    JSONValue **tail = &value->child;
    if (**text != close) {
      while (true) {
        char *key = nullptr;
        if (object) {
          key = string(text);
          if (key == nullptr) {
            goto invalid;
          }
          space(text);
          if (**text != ':' || json_member(value, key) != nullptr) {
            free(key);
            goto invalid;
          }
          ++*text;
        }
        *tail = parse(text, depth + 1);
        if (*tail == nullptr) {
          free(key);
          goto invalid;
        }
        (*tail)->key = key;
        tail = &(*tail)->next;
        space(text);
        if (**text != ',') {
          break;
        }
        ++*text;
        space(text);
      }
    }
    if (**text != close) {
      goto invalid;
    }
    ++*text;
  } else if (strncmp(*text, "null", 4) == 0) {
    *text += 4;
    value->kind = J_NULL;
  } else if (**text >= '0' && **text <= '9') {
    value->kind = J_NUMBER;
    if (**text == '0' && isdigit((unsigned char)(*text)[1])) {
      goto invalid;
    }
    while (**text >= '0' && **text <= '9') {
      unsigned const digit = (unsigned)(**text - '0');
      if (value->number > (UINT64_MAX - digit) / 10) {
        goto invalid;
      }
      value->number = value->number * 10 + digit;
      ++*text;
    }
  } else {
    goto invalid;
  }
  return value;
invalid:
  json_input_destroy(value);
  return nullptr;
}

JSONValue *json_parse_input(char const *text) {
  if (text == nullptr) {
    return nullptr;
  }
  JSONValue *value = parse(&text, 0);
  space(&text);
  if (*text != '\0') {
    json_input_destroy(value);
    return nullptr;
  }
  return value;
}
