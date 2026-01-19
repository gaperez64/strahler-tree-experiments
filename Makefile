all: genstree lenstree pms2dot

genstree: genstree.c printdot.c prtstree.h
	$(CC) -O3 -std=c23 genstree.c printdot.c -o genstree -Wall

pms2dot: pms2dot.c prtstree.h printdot.c
	$(CC) -O3 -std=c23 pms2dot.c printdot.c -o pms2dot -Wall

lenstree: lenstree.cpp
	$(CXX) -Wall -O3 lenstree.cpp -o lenstree -Wall

clean:
	rm genstree lenstree

regtest:
	echo "Running regression tests..." 
	./tests/run-regression.sh
