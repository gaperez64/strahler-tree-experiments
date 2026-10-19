#ifndef CLI_PARSE_HPP
#define CLI_PARSE_HPP 1

#include <charconv>
#include <string_view>
#include <system_error>

[[nodiscard]] inline bool parse_int(char const *text, int minimum,
                                    int &result) {
  std::string_view const input{text};
  int parsed = 0;
  auto const conversion =
      std::from_chars(input.data(), input.data() + input.size(), parsed);
  if (conversion.ec != std::errc{} ||
      conversion.ptr != input.data() + input.size() || parsed < minimum) {
    return false;
  }
  result = parsed;
  return true;
}

#endif
