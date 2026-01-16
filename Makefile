CC=gcc
CXX=g++

all: gstree lenstree

gstree: genstree.c
	$(CC) -std=c23 -Wall -O3 genstree.c -o gstree

lenstree: lenstree.cpp
	$(CXX) -Wall -O3 lenstree.cpp -o lstree

clean:
	rm gstree lstree
