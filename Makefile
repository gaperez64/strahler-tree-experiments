all: gstree lenstree

gstree: genstree.c printdot.c prtstree.h
	$(CC) -O3 -std=c23 genstree.c printdot.c -o gstree -Wall

lenstree: lenstree.cpp
	$(CXX) -Wall -O3 lenstree.cpp -o lstree -Wall

clean:
	rm gstree lstree

regtest:
	echo "Running regression tests..." 
	./tests/run-regression.sh
