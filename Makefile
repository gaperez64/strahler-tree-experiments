CC=gcc

all: gstree 

gstree: genstree.c
	$(CC) -std=c23 -g genstree.c -o gstree

clean:
	rm gstree
