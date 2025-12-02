CC = gcc
CFLAGS = -std=c23 -Wall -Wextra -O2
CFLAGS_DEBUG = -std=c23 -Wall -Wextra -g -fsanitize=address,undefined

TARGET = advent
SRC = advent.c

.PHONY: all clean debug run run1 run2

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $<

debug: $(SRC)
	$(CC) $(CFLAGS_DEBUG) -o $(TARGET) $<

run1: $(TARGET)
	./$(TARGET) 1 ../input.txt

run2: $(TARGET)
	./$(TARGET) 2 ../input.txt

run1-sample: $(TARGET)
	./$(TARGET) 1 ../sample_input.txt

run2-sample: $(TARGET)
	./$(TARGET) 2 ../sample_input.txt

clean:
	rm -f $(TARGET)
