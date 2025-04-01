# Wordle Solver Step 4: Optimizing with Struct-Based Word Representation

In this fourth step, you'll optimize the Wordle solver by changing the word representation from character pointers to a fixed-size struct.

## Learning Objectives

- Understand the performance benefits of contiguous memory layouts
- Practice working with value semantics in C
- Modify existing code to use a different data representation
- Learn how to efficiently store fixed-length strings

## Project Overview

In previous steps, you implemented a vector to store words, feedback functionality, and a suggestion system. In this step, you'll optimize the memory representation of words by:

1. Switching from a string-based representation (`char *`) to a struct-based representation (`struct word`)
2. Updating your code to work with the new representation throughout
3. Simplifying memory management by eliminating individual string allocations

## Files Description

- `main.c`: Updated test program (provided)
- `wordle.h`: Updated header file with new struct definitions (provided)
- `ui.c`: Updated interactive UI that works with the new struct (provided)
- `vector.c`: Update to work with struct word instead of char *
- `read_words.c`: Update to create and populate struct word objects
- `feedback.c`: Update to work with struct word parameters
- `suggest.c`: Update to handle struct word in suggestions

## Implementation Tasks

### 1. Update Vector Implementation (vector.c)

The vector now stores an array of `struct word` objects instead of character pointers:

```c
struct vector {
    struct word *array;  // Changed from char **
    size_t len;
    size_t cap;
};
```

Modify these functions:

#### `struct vector *vector_new(void)`
- Allocate memory for the vector struct
- Update to allocate an array of `struct word` objects instead of `char *` pointers
- Set initial capacity and length as before

#### `void vector_push(struct vector *v, struct word word)`
- Update parameter to accept a `struct word` by value instead of a `char *`
- If needed, resize the array as before
- Copy the word struct directly into the array (no need for malloc or strcpy)
- Increment the vector's length

#### `void vector_free(struct vector *v)`
- Simplify this function since there's no need to free individual strings
- Just free the array and the vector struct

### 2. Update Word Reading (read_words.c)

The `read_words` function now needs to create `struct word` objects:

#### `struct vector *read_words(char *filename)`
- Keep the file reading logic the same
- When a valid word is found, create a `struct word` and copy the string into its `letters` field
- Push the word struct into the vector using the updated `vector_push`

### 3. Update Feedback Implementation (feedback.c)

Update these functions to work with the new word representation:

#### `struct feedback make_feedback(struct word solution, struct word guess)`
- Update parameters to use `struct word` instead of `char *`
- Access letters using `solution.letters[i]` and `guess.letters[i]` syntax
- The rest of the algorithm remains the same

#### `bool is_viable(struct word word, struct feedback feedback)`
- Update parameter to use `struct word` instead of `char *`
- Update letter access to use `word.letters[i]` syntax
- The rest of the algorithm remains the same

#### `bool parse_feedback(char *input, struct feedback *feedback)`
- This function should remain mostly unchanged since it works with strings

### 4. Update Suggestion System (suggest.c)

The `word_score` struct now stores words by value:

```c
struct word_score {
    struct word word;  // Changed from char *
    double score;
};
```

Update these functions:

#### `static int compare_word_scores(const void *a, const void *b)`
- Update to compare the `letters` fields of the word structs
- Use `strcmp(score_a->word.letters, score_b->word.letters)` for alphabetical sorting

#### `struct suggestion_list generate_suggestions(struct vector *dictionary)`
- Update to work with `struct word` parameters and return values
- No need to allocate memory for individual words, just copy the word structs
- The rest of the algorithm remains the same

#### `void free_suggestions(struct suggestion_list *suggestions)`
- Simplify since there's no need to free individual word strings
- Just free the suggestions array

## Implementation Strategy

1. Start with `vector.c`, as it's the foundation of the data structure
2. Then update `read_words.c` to create the word structs properly
3. Update `feedback.c` to work with the new representation
4. Finally, update `suggest.c` to handle the struct-based words

## Testing Your Code

The provided `main.c` includes comprehensive tests for the new struct word implementation. It tests:
- Basic struct word operations
- Vector operations with struct words
- String-to-word conversion
- Feedback system with the new representation
- Suggestion generation and memory management

Run the tests frequently to make sure each part is working before moving on.

## Common Mistakes

1. **Forgetting the Null Terminator**: Remember that `struct word` contains a 6-character array to store 5 letters plus the null terminator
2. **Incorrect String Comparisons**: Use `strcmp()` on the `letters` field, not on the struct itself
3. **Forgetting Value Semantics**: Words are now passed by value, not by pointer
4. **Copying Problems**: Make sure to properly copy the word struct when needed
5. **Memory Management**: No need to allocate or free individual strings anymore

## Expected Improvements

This optimization should:
- Reduce memory fragmentation by using fewer, larger allocations
- Improve cache locality by storing words in contiguous memory
- Simplify memory management by eliminating individual string allocations
- Potentially improve performance through better memory access patterns

Good luck with your optimization!


I suggest making a copy of this version before moving on to step 5,
as it will be another optimization step and you will want the
ability to compare your results.

Remember, to get a speed test you can run:

    echo | time make run
