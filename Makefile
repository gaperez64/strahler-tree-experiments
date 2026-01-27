all: genstree lenstree pms2dot

genstree: genstree.c printdot.c prtstree.h
	$(CC) -O3 -std=c23 genstree.c printdot.c -o genstree -Wall -Wextra -Wpedantic

pms2dot: pms2dot.c prtstree.h printdot.c
	$(CC) -O3 -std=c23 pms2dot.c printdot.c -o pms2dot -Wall -Wextra -Wpedantic

lenstree: lenstree.cpp
	$(CXX) -Wall -O3 lenstree.cpp -o lenstree -Wall -Wextra -Wpedantic

clean:
	rm genstree lenstree pms2dot

regtest:
	echo "Running regression tests..." 
	./tests/run-regression.sh
