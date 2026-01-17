CC=gcc

all: gstree 

gstree: genstree.c
	$(CC) -O3 -std=c23 genstree.c -o gstree

clean:
	rm gstree
