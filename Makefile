CFLAGS=-O3 -std=c23 -Wall -Wextra -Wpedantic -DNDEBUG
CXXFLAGS=-O3 -Wall -Wextra -Wpedantic

all: genstree lenstree pms2dot

genstree: genstree.c prtstree.c prtstree.h
	$(CC) $(CFLAGS) genstree.c prtstree.c -o genstree

pms2dot: pms2dot.c prtstree.h prtstree.c
	$(CC) $(CFLAGS) pms2dot.c prtstree.c -o pms2dot

lenstree: lenstree.cpp
	$(CXX) $(CXXFLAGS) lenstree.cpp -o lenstree

clean:
	rm genstree lenstree pms2dot

regtest:
	echo "Running regression tests..." 
	./tests/run-regression.sh
