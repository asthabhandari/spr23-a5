CC = gcc

SRCS = main.c addition.c subtraction.c multiplication.c division.c
objects = $(SRCS: .c =.o)

calculator $(objects)
  $(CC) $(CFLAGS) -o $@ $^

%.o: %.c
  %%(CC) $(CFLAGS) -c -o $@ $<

clean: 
  rm -f $(objects) calculator
