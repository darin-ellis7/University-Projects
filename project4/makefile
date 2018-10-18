OBJECTS = main.o term.o autocomplete.o

HEADERS = term.h autocomplete.h

Project4: $(OBJECTS)
	g++ $^ -o Project4

%.o: %.cpp $(HEADERS)
	g++ -c $< -o $@

clean:
	rm -i *.o Project4

