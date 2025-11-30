#define _POSIX_C_SOURCE 200809L

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void print_usage(char *argv[]) {
  fprintf(stderr, "Usage: %s -k K -t T -h H \n", argv[0]);
}

typedef struct _node {
  int k;
  int t;
  int h;
  short u;
} Node;

#define PUSH(UVAL, KVAL, TVAL, HVAL, LENQ, MAXQ, STACK)                        \
  do {                                                                         \
    if (LENQ >= MAXQ) {                                                        \
      MAXQ = 2 * (MAXQ + 1);                                                   \
      STACK = realloc(STACK, MAXQ * sizeof(*STACK));                           \
      assert(LENQ < MAXQ);                                                     \
    }                                                                          \
    STACK[LENQ].u = ((UVAL) == 0);                                             \
    STACK[LENQ].k = KVAL;                                                      \
    STACK[LENQ].t = TVAL;                                                      \
    STACK[LENQ].h = HVAL;                                                      \
    LENQ++;                                                                    \
    assert(LENQ <= MAXQ);                                                      \
  } while (0)

unsigned strahler_tree(int k, int t, int h) {
  assert(h >= k);
  unsigned (*tree)[k + 1][t + 1][h + 1] = calloc(2, sizeof(*tree));
  const short UTREE = 0;
  const short VTREE = 1;

  size_t maxq = 0;
  size_t lenq = 0;
  Node *stack = nullptr;

  // this is the node of interest
  PUSH(0, k, t, h, lenq, maxq, stack);

  while (lenq > 0) {
    Node tos = stack[lenq - 1];
    if (tos.u && tos.h == 1 && tos.k == 1) {
      tree[UTREE][tos.k][tos.t][tos.h] = 1;
      lenq--; // pop
    } else if (tos.u && tos.h > 1 && tos.k == 1) {
      unsigned son = tree[UTREE][tos.k][tos.t][tos.h - 1];
      if (son > 0) {
        tree[UTREE][tos.k][tos.t][tos.h] = son;
        lenq--; // pop
      } else {
        PUSH(0, tos.k, tos.t, tos.h - 1, lenq, maxq, stack);
      }
    } else if (tos.h >= tos.k && tos.k >= 2 && tos.t == 0) {
      unsigned son = tree[UTREE][tos.k - 1][tos.t][tos.h - 1];
      if (son > 0) {
        tree[tos.u ? 0 : 1][tos.k][tos.t][tos.h] = son;
        lenq--; // pop
      } else {
        PUSH(0, tos.k - 1, tos.t, tos.h - 1, lenq, maxq, stack);
      }
    } else if (!tos.u && tos.h >= tos.k && tos.k >= 2 && tos.t >= 1) {
      unsigned child1 = tree[VTREE][tos.k][tos.t - 1][tos.h];
      unsigned child2 = tree[UTREE][tos.k - 1][tos.t][tos.h - 1];
      if (child1 > 0 && child2 > 0) {
        tree[VTREE][tos.k][tos.t][tos.h] = child1 * 2 + child2;
        lenq--; // pop
      } else {
        PUSH(1, tos.k, tos.t - 1, tos.h, lenq, maxq, stack);
        PUSH(0, tos.k - 1, tos.t, tos.h - 1, lenq, maxq, stack);
      }
    } else if (tos.u && tos.h == tos.k && tos.k >= 2) {
      unsigned son = tree[VTREE][tos.k][tos.t][tos.h];
      if (son > 0) {
        tree[UTREE][tos.k][tos.t][tos.h] = son;
        lenq--; // pop
      } else {
        PUSH(1, tos.k, tos.t, tos.h, lenq, maxq, stack);
      }
    } else if (tos.u && tos.h > tos.k && tos.k >= 2) {
      unsigned child1 = tree[VTREE][tos.k][tos.t][tos.h];
      unsigned child2 = tree[UTREE][tos.k][tos.t][tos.h - 1];
      if (child1 > 0 && child2 > 0) {
        tree[UTREE][tos.k][tos.t][tos.h] = child1 * 2 + child2;
        lenq--; // pop
      } else {
        PUSH(1, tos.k, tos.t, tos.h, lenq, maxq, stack);
        PUSH(0, tos.k, tos.t, tos.h - 1, lenq, maxq, stack);
      }
    } else {
      assert(false);
    }
  }

  unsigned total = tree[UTREE][k][t][h];
  printf("U^%d_{%d,%d} has %d leaves\n", k, t, h, total);

  // Epilogue
  free(stack);
  free(tree);

  return total;
}

int main(int argc, char *argv[]) {
  int opt;
  int k;
  int t;
  int h;
  bool kset = false;
  bool tset = false;
  bool hset = false;

  while ((opt = getopt(argc, argv, "k:t:h:")) != -1) {
    switch (opt) {
    case 'k':
      k = atoi(optarg);
      if (k < 1) {
        fprintf(stderr, "K must be a positive integer\n");
        return EXIT_FAILURE;
      }
      kset = true;
      break;
    case 't':
      t = atoi(optarg);
      if (t < 0) {
        fprintf(stderr, "T must be a nonnegative integer\n");
        return EXIT_FAILURE;
      }
      tset = true;
      break;
    case 'h':
      h = atoi(optarg);
      if (h < 1) {
        fprintf(stderr, "H must be a positive integer\n");
        return EXIT_FAILURE;
      }
      hset = true;
      break;
    default: /* '?' */
      print_usage(argv);
      return EXIT_FAILURE;
    }
  }

  if (!(kset && tset && hset)) {
    fprintf(stderr, "Expected three arguments\n");
    print_usage(argv);
    return EXIT_FAILURE;
  }

  // Continuing with the actual computation of the
  unsigned nleaves = strahler_tree(k, t, h);

  return EXIT_SUCCESS;
}
