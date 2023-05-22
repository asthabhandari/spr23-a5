objects = main.o addition.o subtraction.o multiplication.o division.o

calculator: $(objects)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(objects) calculator
