#ifndef TRACE_ALLOCATOR_H
#define TRACE_ALLOCATOR_H 1

#include <stdlib.h>

void *trace_test_malloc(size_t size);
void *trace_test_calloc(size_t count, size_t size);
void *trace_test_realloc(void *data, size_t size);

#define malloc trace_test_malloc
#define calloc trace_test_calloc
#define realloc trace_test_realloc

#endif
