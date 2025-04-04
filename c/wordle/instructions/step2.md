Wordle solver step 2
====================

In this second step, you'll implement functions that handle Wordle game feedback - the colored hints that show which letters are correct (green), in the wrong position (yellow), or not in the word (gray).

Learning Objectives
-------------------

* Implement complex algorithms with multiple passes
* Work with enums and structured data in C
* Process character-based input with various formats
* Develop test cases for different scenarios

Project Overview
----------------

Building on your vector implementation from Step 1, you'll now add:

1. A function to generate feedback by comparing a guess with a solution
2. A function to determine if a word is still a viable guess based on feedback
3. A function to parse user input into a feedback structure

Files Description
-----------------

* `main.c`: Test program (provided)
* `wordle.h`: Header file with definitions (provided)
* `feedback.c`: Implement your feedback functions here

Implementation Tasks
--------------------

### 1. Feedback Structure

The header file already provides these types:

```c
enum wordle_color {
    COLOR_GRAY,     // no
    COLOR_YELLOW,   // yes but wrong position
    COLOR_GREEN     // yes
};

struct letter_feedback {
    char letter;
    enum wordle_color color;
};

struct feedback {
    struct letter_feedback letters[5];
};
```

### 2. Feedback Implementation

Implement these three functions in `feedback.c`:

#### `struct feedback make_feedback(char *solution, char *guess)`

Generates feedback by comparing a guess with the solution:
- Create a feedback structure for a 5-letter guess
- Mark letters as green if they match the solution at the same position
- Mark letters as yellow if they appear in the solution but at a different position
- Mark remaining letters as gray
- Handle duplicate letters correctly (once a solution letter is "used" for feedback, it can't be used again)

Implementation approach:
- Make a copy of the solution so you can mark letters as used
- First pass: Check for exact matches (green)
- Second pass: Check for letters in wrong positions (yellow)
- Return the completed feedback structure

#### `bool is_viable(char *word, struct feedback feedback)`

Determines if a word is still a viable guess based on feedback:
- Return true if the word is consistent with the feedback
- Return false if the word contradicts any part of the feedback

Implementation approach:
- Make a copy of the word so you can mark letters as checked
- First pass: Check green (exact match) and yellow (position mismatch) constraints
- Second pass: Check yellow letters exist somewhere in the word
- Third pass: Check gray letters don't appear anywhere in the remaining word
- Return true only if all constraints are satisfied

#### `bool parse_feedback(char *input, struct feedback *feedback)`

Parses a line of user input into a feedback structure:
- Return true if the input is valid
- Return false if the input is invalid

Input format:
- GREEN letters: uppercase ('A' to 'Z'), converted to lowercase
- YELLOW letters: preceded by '.' or space, then lowercase ('a' to 'z')
- GRAY letters: lowercase ('a' to 'z')
- Example: "A.bc.d" means:
  - 'a' is GREEN
  - 'b' is YELLOW
  - 'c' is GRAY
  - 'd' is YELLOW

### Error Handling Guidelines

- For invalid input in `parse_feedback`, simply return false
- Assume both `solution` and `guess` are valid 5-letter lowercase strings
- No need to handle malloc/free as these functions work with stack-allocated data

Implementation Strategy
-----------------------

We recommend implementing in this order:

1. `make_feedback()` - Test it by running `./wordle`
2. `is_viable()` - Test it after implementation
3. `parse_feedback()` - Test it after everything else works

Testing Your Code
-----------------

The provided `main.c` runs all tests in sequence. Each test function:
- Defines multiple test cases with expected results
- Calls your implementation with the test data
- Prints detailed information about each test case
- Indicates whether each test passes or fails

Common Mistakes
---------------

1. **Duplicate Letters**: A common edge case is handling duplicate letters correctly
   - Example: For guess "hello" and solution "apple", only one 'l' should be yellow
   - Once a solution letter is "used" for feedback, it can't be used again

2. **Precedence Rules**:
   - Green matches have precedence over yellow
   - Earlier positions have precedence for yellow matches

3. **Viable Word Checking**:
   - A word is viable only if it satisfies all constraints from the feedback
   - Gray letters must not appear anywhere (unless also marked green/yellow elsewhere)
   - Yellow letters must appear somewhere, but not at the marked position
   - Green letters must appear exactly at the marked position

4. **Input Parsing**:
   - Carefully check the format examples
   - Pay attention to yellow letter format (preceded by '.' or space)
   - Validate input length and character types

Advanced Considerations
-----------------------

- Consider the Wordle rules for duplicate letters (if "guess" has multiple instances but "solution" has only one)
- Think about the algorithm's efficiency, especially for the `is_viable` function
- Make sure your implementation handles edge cases correctly

Good luck with your implementation!
