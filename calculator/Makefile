CFLAGS = -Wall -Werror -g
objects = main.o addition.o subtraction.o multiplication.o division.o

.PHONY: all clean 

all: calculator 

calculator: $(objects)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(objects) calculator
