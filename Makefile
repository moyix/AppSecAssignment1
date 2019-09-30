default: prog

get-deps:
	# Assuming Debian or Ubuntu here
	sudo apt-get install -y build-essential check

dictionary.o: dictionary.c
	gcc -Wall -c dictionary.c dictionary.h

spell.o: spell.c
	gcc -Wall -c spell.c

test.o: test_main.c
	gcc -Wall -c test_main.c

main.o: main.c
	gcc -Wall -c main.c

test: dictionary.o spell.o test_main.o
	gcc -Wall -o test_main test_main.o spell.o dictionary.o `pkg-config --cflags --libs check`
	./test_main

prog: dictionary.o spell.o main.o
	gcc -Wall -o spell_check dictionary.o spell.o main.o

autograder: dictionary.o spell.o main.o
	gcc -Wall -o a.out dictionary.o spell.o main.o
	python3 run_tests.py

clean:
	rm -f dictionary.o spell.o main.o test_main.o a.out spell_check test_main *.gch
