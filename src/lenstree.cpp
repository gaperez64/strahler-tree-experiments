#include <boost/functional/hash.hpp>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <getopt.h>
#include <iostream>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

#include "cli_parse.hpp"
#include "cli_version.h"

struct Node {
  int k;
  int t;
  int h;
  bool isU;
};

// Keep track of already computed sizes, this is cached beyond single calls of
// tree_size below
std::unordered_map<std::tuple<int, int, int>, unsigned,
                   boost::hash<std::tuple<int, int, int>>>
    treeU;
std::unordered_map<std::tuple<int, int, int>, unsigned,
                   boost::hash<std::tuple<int, int, int>>>
    treeV;

// Leaf counts saturate at UINT_MAX instead of wrapping around.
static unsigned saturating_leaf_sum(unsigned repeated, unsigned middle) {
  if (repeated > (UINT_MAX - middle) / 2) {
    return UINT_MAX;
  }
  return repeated * 2 + middle;
}

unsigned tree_size(int k, int t, int h, bool isU) {
  std::cout << "Looking into k=" << k << ", t=" << t << ", h=" << h
            << std::endl;
  // Check for cache hit
  auto &requested_tree = isU ? treeU : treeV;
  auto cached = requested_tree.find(std::make_tuple(k, t, h));
  if (cached != requested_tree.end()) {
    return cached->second;
  }

  std::stack<Node> stack;

  stack.push({k, t, h, isU});
  while (!stack.empty()) {
    Node &tos = stack.top();
    if (tos.isU and tos.h == 1 and tos.k == 1) {
      treeU[std::make_tuple(tos.k, tos.t, tos.h)] = 1;
      stack.pop();
    } else if (tos.isU and tos.h > 1 and tos.k == 1) {
      auto son = treeU.find(std::make_tuple(tos.k, tos.t, tos.h - 1));
      if (son != treeU.end()) {
        treeU[std::make_tuple(tos.k, tos.t, tos.h)] = son->second;
        stack.pop();
      } else
        stack.push({tos.k, tos.t, tos.h - 1, true});
    } else if (tos.h >= tos.k and tos.k >= 2 and tos.t == 0) {
      auto son = treeU.find(std::make_tuple(tos.k - 1, tos.t, tos.h - 1));
      if (son != treeU.end()) {
        if (tos.isU)
          treeU[std::make_tuple(tos.k, tos.t, tos.h)] = son->second;
        else
          treeV[std::make_tuple(tos.k, tos.t, tos.h)] = son->second;
        stack.pop();
      } else
        stack.push({tos.k - 1, tos.t, tos.h - 1, true});
    } else if (!tos.isU and tos.h >= tos.k and tos.k >= 2 and tos.t >= 1) {
      auto son1 = treeV.find(std::make_tuple(tos.k, tos.t - 1, tos.h));
      auto son2 = treeU.find(std::make_tuple(tos.k - 1, tos.t, tos.h - 1));
      if (son1 != treeV.end() and son2 != treeU.end()) {
        treeV[std::make_tuple(tos.k, tos.t, tos.h)] =
            saturating_leaf_sum(son1->second, son2->second);
        stack.pop();
      } else {
        stack.push({tos.k - 1, tos.t, tos.h - 1, true});
        stack.push({tos.k, tos.t - 1, tos.h, false});
      }
    } else if (tos.isU and tos.h == tos.k and tos.k >= 2) {
      auto son = treeV.find(std::make_tuple(tos.k, tos.t, tos.h));
      if (son != treeV.end()) {
        treeU[std::make_tuple(tos.k, tos.t, tos.h)] = son->second;
        stack.pop();
      } else
        stack.push({tos.k, tos.t, tos.h, false});
    } else if (tos.isU and tos.h > tos.k and tos.k >= 2) {
      auto son1 = treeV.find(std::make_tuple(tos.k, tos.t, tos.h));
      auto son2 = treeU.find(std::make_tuple(tos.k, tos.t, tos.h - 1));
      if (son1 != treeV.end() and son2 != treeU.end()) {
        treeU[std::make_tuple(tos.k, tos.t, tos.h)] =
            saturating_leaf_sum(son1->second, son2->second);
        stack.pop();
      } else {
        stack.push({tos.k, tos.t, tos.h - 1, true});
        stack.push({tos.k, tos.t, tos.h, false});
      }
    } else
      assert(false); // We should never get here
  }

  return isU ? treeU[std::make_tuple(k, t, h)]
             : treeV[std::make_tuple(k, t, h)];
}

std::pair<std::vector<bool>, std::vector<int>> label_lth_leaf(int k, int t,
                                                              int h, int lth) {
  std::pair<std::vector<bool>, std::vector<int>> leaf;
  Node node{k, t, h, true};
  unsigned lth_tmp = static_cast<unsigned>(lth);

  while (true) {
    if (node.isU and node.k == 1) {
      assert(lth_tmp == 1);
      // Just empty string... (We can combine case 1 and 2 from the C)
      break;
    } else if (node.h >= node.k and node.k >= 2 and node.t == 0) {
      if (node.isU) {
        leaf.first.push_back(0);
        leaf.second.push_back(h - node.h); // Double check!
      }
      node.isU = true;
      node.k--;
      node.h--;
    } else if (!node.isU and node.h >= node.k and node.k >= 2 and node.t >= 1) {
      unsigned size_child1 = tree_size(node.k, node.t - 1, node.h, false);
      unsigned size_child2 = tree_size(node.k - 1, node.t, node.h - 1, true);
      if (size_child1 >= lth_tmp) {
        leaf.first.push_back(0);
        leaf.second.push_back(h - node.h); // Double check!
        node.t--;
        node.isU = false;
      } else if (lth_tmp - size_child1 <= size_child2) {
        lth_tmp -= size_child1;
        node.isU = true;
        node.k--;
        node.h--;
      } else {
        lth_tmp -= size_child1;
        lth_tmp -= size_child2;
        leaf.first.push_back(1);
        leaf.second.push_back(h - node.h); // Double check!
        node.isU = false;
        node.t--;
      }
    } else if (node.isU and node.h == node.k and node.k >= 2) {
      leaf.first.push_back(0);
      leaf.second.push_back(h - node.h); // Double check!
      node.isU = false;
    } else if (node.isU and node.h > node.k and node.k >= 2) {
      unsigned size_child1 = tree_size(node.k, node.t, node.h, false);
      unsigned size_child2 = tree_size(node.k, node.t, node.h - 1, true);
      if (size_child1 >= lth_tmp) {
        leaf.first.push_back(0);
        leaf.second.push_back(h - node.h); // Double check!
        node.isU = false;
      } else if (lth_tmp - size_child1 <= size_child2) {
        lth_tmp -= size_child1;
        node.isU = true;
        node.h--;
      } else {
        lth_tmp -= size_child1;
        lth_tmp -= size_child2;
        leaf.first.push_back(1);
        leaf.second.push_back(h - node.h); // Double check!
        node.isU = false;
      }
    } else {
      assert(false);
    }
  }

  return leaf;
}

static void print_usage(FILE *out, char *argv[]) {
  cli_usage(out, argv[0], "");
  fputs("  --strahler=K                                Strahler parameter "
        "(required, 1 <= K <= H)\n"
        "  --height=H                                  Tree height (required, "
        "H >= 1)\n"
        "  --log-leaves=T                              Leaf-budget exponent "
        "(required, T >= 0)\n"
        "  --leaf=L                                    Print the L-th leaf "
        "(1-based; default: count)\n",
        out);
}

int main(int argc, char **argv) {
  static struct option const options[] = {
      {"help", no_argument, nullptr, 1},
      {"version", no_argument, nullptr, 'v'},
      {"strahler", required_argument, nullptr, 'k'},
      {"log-leaves", required_argument, nullptr, 't'},
      {"height", required_argument, nullptr, 'h'},
      {"leaf", required_argument, nullptr, 'l'},
      {nullptr, 0, nullptr, 0},
  };
  int opt;
  int k = 0;
  int t = 0;
  int h = 0;
  int l = 0;
  bool kset = false;
  bool tset = false;
  bool hset = false;
  bool lset = false;

  while ((opt = cli_getopt(argc, argv, options)) != -1) {
    switch (opt) {
    case 1:
      print_usage(stdout, argv);
      return EXIT_SUCCESS;
    case 'v':
      return cli_print_version(argv[0]);
    case 'k':
      if (!parse_int(optarg, 1, k)) {
        return cli_error(argv[0], "--strahler must be a positive integer");
      }
      kset = true;
      break;
    case 't':
      if (!parse_int(optarg, 0, t)) {
        return cli_error(argv[0], "--log-leaves must be a nonnegative integer");
      }
      tset = true;
      break;
    case 'h':
      if (!parse_int(optarg, 1, h)) {
        return cli_error(argv[0], "--height must be a positive integer");
      }
      hset = true;
      break;
    case 'l':
      if (!parse_int(optarg, 1, l)) {
        return cli_error(argv[0], "--leaf must be a positive integer");
      }
      lset = true;
      break;
    default: /* '?' */
      return cli_error(argv[0],
                       "Unknown option or invalid argument; use --name=value");
    }
  }

  if (optind != argc) {
    return cli_error(argv[0], "Unexpected operand");
  }
  if (hset && kset && h < k) {
    return cli_error(argv[0], "--height must be at least --strahler");
  }
  if (!(kset && tset && hset)) {
    return cli_error(argv[0],
                     "--strahler, --log-leaves and --height are required");
  }

  if (lset) {
    if (std::cmp_greater(l, tree_size(k, t, h, true))) {
      return cli_error(argv[0], "--leaf exceeds the number of leaves");
    }
    auto leaf = label_lth_leaf(k, t, h, l);
    std::cout << "Leaf no " << l << " is ";
    std::cout << std::noboolalpha;
    for (bool bit : leaf.first) {
      std::cout << bit;
    }
    std::cout << std::boolalpha << " ";
    for (int lvl : leaf.second) {
      std::cout << lvl;
    }
    std::cout << std::endl;
  } else {
    unsigned len = tree_size(k, t, h, true);
    std::cout << "It has " << len << " leaves\n";
  }

  return EXIT_SUCCESS;
}
