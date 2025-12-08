CC=gcc

all: gstree 

gstree: genstree.c
	$(CC) -std=c23 -Wall -O3 genstree.c -o gstree

clean:
	rm gstree
