#include <cassert>
#include <limits>
#include <string>

#include "cli_parse.hpp"

int main() {
  int value = -1;
  assert(parse_int("0", 0, value) && value == 0);
  assert(parse_int("42", 1, value) && value == 42);
  std::string const maximum = std::to_string(std::numeric_limits<int>::max());
  assert(parse_int(maximum.c_str(), 0, value));
  for (char const *invalid :
       {"", "-1", "+1", " 1", "1 ", "1x", "999999999999999999999"}) {
    assert(!parse_int(invalid, 0, value));
    assert(value == std::numeric_limits<int>::max());
  }
  assert(!parse_int("0", 1, value));
}
