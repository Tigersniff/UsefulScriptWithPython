CC=gcc
OBJECT=$(wildcard *.c)
TARGET=$(OBJECT:%.c=%.o)

.PHONY: all clean


all:  $(TARGET)

clean:
	rm -rf *.o

%.o: %.c
	$(CC) -o $@ $^
