Wordle solver step 1
====================

In this first step, you'll implement a string vector data structure and functions to read Wordle words from a file.

Learning Objectives
-------------------

- Implement a dynamic array (vector) in C
- Practice memory management with `malloc`, `realloc`, and `free`
- Work with file I/O and string processing
- Handle errors appropriately

Project Overview
----------------

The Wordle Helper will assist in solving the Wordle game by suggesting optimal word guesses. For this step, you'll build:

1. A dynamic string vector to store words
2. Functions to read valid Wordle words from a file

Files Description
-----------------

- `main.c`: Test program (provided)
- `wordle.h`: Header file with definitions (provided)
- `vector.c`: Implement your vector functions here
- `read_words.c`: Implement your word reading function here

Implementation Tasks
--------------------

### 1. Vector Implementation

First, implement these functions in `vector.c`:

#### `struct vector *vector_new(void)`

Creates a new, empty vector:
- Allocate memory for the vector struct using `malloc`
- Set initial capacity to 16 elements
- Set initial length to 0
- Allocate memory for the array of string pointers
- Return the new vector

#### `void vector_push(struct vector *v, char *str)`

Adds a string to the end of a vector:
- If the vector is full (length equals capacity), double the capacity using `realloc`
- Allocate memory for a copy of the string (remember the null terminator)
- Copy the string using `strcpy`
- Increment the vector's length

#### `void vector_free(struct vector *v)`

Frees all memory associated with a vector:
- Free each string in the array
- Free the array itself
- Free the vector struct
- Set pointers to NULL to prevent use after free

### 2. Word Reading Implementation

Next, implement the function in `read_words.c`:

#### `struct vector *read_words(char *filename)`

Reads valid words from a file:
- Open the specified file with `fopen`
- Read the file line by line with `fgets`
- For each line:
  - Remove the trailing newline character
  - Check if the word is valid using the provided `is_valid_word` function
  - Skip invalid words with a warning message to stdout
  - Add valid words to a vector
- Close the file and return the vector

### Error Handling Guidelines

- Fatal errors: Use `fprintf(stderr, ...)` followed by `exit(1)`
  - Examples: failed memory allocations, cannot open file
- Warnings: Use `printf(...)` and continue execution
  - Examples: invalid words, no valid words found

Important: Writing to stderr will cause tests to fail. Only use stderr for truly fatal errors.

Implementation Strategy
-----------------------

We recommend implementing in this order:

1. `vector_new()` - Test it by running `make run`
2. `vector_push()` - Test it after implementation
3. `vector_free()` - Test it after implementation
4. `read_words()` - Test it after everything else works

Testing Your Code
-----------------

The provided `main.c` runs all tests in sequence. Each test function will:
- Print information about what it's testing
- Call your implementation
- Print results that can be verified

When you start, you'll see "not implemented" errors. As you implement each function, these errors will be replaced with actual test results.

You don't need to modify the test code or create new tests.

Common Mistakes
---------------

1. **Memory Leaks**: Always match `malloc` with `free`
2. **Buffer Overflow**: Watch string lengths and allocate properly
3. **String Termination**: Remember to include space for the null terminator (`\0`)
4. **Vector Capacity**: Double the capacity when needed, not just increment it
5. **Error Handling**: Check return values from `malloc`, `realloc`, and `fopen`

Testing Tips
------------

- Test each function immediately after implementing it
- Use `valgrind` to detect memory leaks (if available)
- Add temporary debug print statements if needed
- Check edge cases (empty files, exactly-full vectors)

Good luck with your implementation!
