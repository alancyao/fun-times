CC = g++
CFLAGS = -g -std=c++0x -O3 -Wall -DGL_GLEXT_PROTOTYPES -IEigen/
LDFLAGS = -g -std=c++0x -Wall -lglut -lGLU -lSOIL

RM = /bin/rm -f
all: main

TARGET = fractal
main: Main.o 
	$(CC) $(CFLAGS) -o $(TARGET) $^ $(LDFLAGS)
%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) *.o $(TARGET) 
