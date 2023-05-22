CC = gcc
CFLAGS = -Wall -Werror 

SRCS = main.c addition.c subtraction.c multiplication.c division.c
OBJS = $(SRCS: .c =.o)

calculator $(OBJS)
  $(CC) $(CFLAGS) -o $@ $^

%.o: %.c
  %%(CC) $(CFLAGS) -c -o $@ $<

clean: 
  rm -f $(OBJS) calculator
