I'll provide an updated version of the instructions that quotes directly from the provided files where helpful:

# Wordle Helper Project Step 5: Bit Vector Optimization

## Introduction to Bit Vector Optimization

In this final step, we'll implement a powerful optimization to make our Wordle helper run much faster. So far, the program works correctly but can be slow, especially when handling large dictionaries. The main bottleneck is in the `is_viable` function, which is called an enormous number of times during suggestion generation.

### Understanding the Problem

Our current algorithm has a time complexity of O(n³), where n is the number of words in the dictionary:
- For each possible guess (n words)
  - For each possible solution (n words)
    - For each remaining word in the dictionary (n words)
      - Check if it's viable given the feedback

This cubic complexity is even more severe than it sounds. For the standard Wordle dictionary of about 13,000 words, the inner loop can run around 2 trillion times! Even with the smaller "solution" dictionary of 2,315 words, the inner loop may run over 12 billion times when generating a starter word suggestion. This makes the optimization extremely important.

### The Bit Vector Solution

We'll implement a "pre-screening" step using bit vectors (also called bit masks). This technique allows us to quickly eliminate most non-viable words before running the more expensive character-by-character comparison in `is_viable`.

**What is a bit vector?**
A bit vector is a sequence of bits where each bit represents a boolean value (true/false). In our case, we'll use a 64-bit integer (`uint64_t`) where:
- The lower 32 bits indicate which letters are present in a word
- The upper 32 bits indicate which letters are explicitly excluded

This works because there are only 26 letters in the alphabet, so we can assign one bit per letter. For example:
- If a word contains 'a', we set bit 0
- If a word contains 'b', we set bit 1
- And so on...

**Why is this faster?**
Modern CPUs can perform bitwise operations (AND, OR, XOR) on 64-bit values in a single instruction. This is much faster than iterating through characters and comparing them individually.

**How will it work?**
1. For each word, we'll pre-compute a bit mask showing which letters it contains
2. For each feedback pattern, we'll generate a bit mask showing:
   - Which letters must be present (green/yellow letters)
   - Which letters must be absent (gray letters)
3. Before calling the full `is_viable` function, we'll do a quick bitwise check that can eliminate most non-viable words in a single CPU operation

## Files That Need Changes

In this step, you'll need to modify:
- `read_words.c` - To initialize the bit mask when reading words
- `feedback.c` - To add the bit mask optimization to the feedback logic
- `suggest.c` - To use the bit mask for pre-screening in the suggestion generation

You'll be provided with updated versions of `wordle.h`, `main.c`, and `ui.c`. Note that `vector.c` does not require any changes.

You'll be working with your own code from previous steps, so some details might vary, but the overall structure should be similar to what's described here.

## Understanding the Updated Word Structure

Let's look at the updated `struct word` definition from `wordle.h`:

```c
struct word {
    char letters[6];  /* 5 letters plus null terminator */
    uint64_t mask;    /* Bit mask for quick filtering */
};
```

The new `mask` field is a 64-bit unsigned integer that will store:
- Which letters are in the word (in the lower 32 bits)
- Information about excluded letters (in the upper 32 bits)

The header file also includes a new function declaration:

```c
/* New addition: Generate a bit mask from a feedback structure */
uint64_t feedback_to_mask(struct feedback *feedback);
```

This function will convert a feedback structure into a bit mask that can be used for quick filtering.

## Implementation Steps

### 1. Update read_words.c to Initialize Bit Masks

In your `read_words` function, you need to initialize the bit mask for each word you read from the file. After you've copied the word into the `letters` field of your word structure, add code to compute and initialize the mask.

You can look at how the updated `str_to_word` helper function in `main.c` handles this:

```c
static struct word str_to_word(const char *str) {
    struct word result;
    strcpy(result.letters, str);

    // Initialize the bit mask
    uint64_t mask = 0;
    for (int i = 0; i < WORD_LENGTH; i++) {
        char ch = str[i];
        mask |= 1ULL << (ch - 'a');
        mask |= 1ULL << ((ch - 'a') + 32);
    }
    result.mask = mask;

    return result;
}
```

Follow this pattern in your `read_words` function:
1. Initialize a mask to 0
2. For each letter in the word:
   - Set the corresponding bit in the lower 32 bits: `mask |= 1ULL << (letter - 'a')`
   - Set the corresponding bit in the upper 32 bits: `mask |= 1ULL << ((letter - 'a') + 32)`
3. Store the computed mask in the word structure

### 2. Implement the feedback_to_mask Function in feedback.c

Add a new function to `feedback.c` that generates a bit mask from a feedback structure:

```c
uint64_t feedback_to_mask(struct feedback *feedback) {
    // Your implementation here
}
```

Your implementation should:
1. Initialize an `expected` mask to 0 (this will hold bits for letters that must be present)
2. For each letter in the feedback:
   - If it's green or yellow, set its bit in the `expected` mask
3. Initialize a `mask` to the value of `expected`
4. For each gray letter in the feedback:
   - If its bit is not set in `expected` (meaning it's not required elsewhere),
     set the corresponding bit in the upper 32 bits of `mask`
5. Return the final `mask`

The new test function in `main.c` demonstrates how this should work:

```c
// Generate mask from feedback
uint64_t mask = feedback_to_mask(&feedback);
uint64_t expected = mask & 0xFFFFFFFF;  // Lower 32 bits

printf("\nGenerated mask: 0x%016llx\n", (unsigned long long)mask);
printf("Expected bits: 0x%016llx\n", (unsigned long long)expected);
```

### 3. Modify is_viable to Use Bit Masks in feedback.c

Now, update the `is_viable` function to use the bit mask for pre-screening. At the beginning of the function, before any of the existing code:

1. Generate a mask from the feedback using your new function
2. Extract the lower 32 bits as the "expected" bits (letters that must be present)
3. Perform a quick pre-screening check: `if ((word.mask & mask) != expected) return false;`
4. If the word passes the pre-screen, continue with the existing detailed checks

The updated test function in `main.c` shows how this should work:

```c
// Test pre-screening with masks
printf("\nTesting pre-screening with masks:\n");
printf("  %s: mask & word.mask = 0x%016llx, expected = 0x%016llx, %s\n",
       word1.letters,
       (unsigned long long)(word1.mask & mask),
       (unsigned long long)expected,
       (word1.mask & mask) == expected ? "PASS" : "FAIL");
```

### 4. Modify calculate_remaining_words in suggest.c

Finally, update the `calculate_remaining_words` function to also use the bit mask optimization. After generating feedback for the guess and solution:

1. Create a mask using `feedback_to_mask`
2. Extract the expected bits (lower 32 bits)
3. In the loop that checks each word, add the pre-screening check before calling `is_viable`

The updated `main.c` checks if your implementation works correctly:

```c
// Compare pre-screening with full is_viable check
printf("\nComparing pre-screening with full is_viable check:\n");

// Create another 3 test words
struct word test_words[3];
test_words[0] = str_to_word("sweet"); // Should be viable
test_words[1] = str_to_word("truck"); // Should not be viable
test_words[2] = str_to_word("sword"); // Should be viable

for (int i = 0; i < 3; i++) {
    bool prescreen_pass = (test_words[i].mask & mask) == expected;
    bool viable = is_viable(test_words[i], feedback);

    printf("  %s: Prescreen %s, Full check %s\n",
           test_words[i].letters,
           prescreen_pass ? "PASS" : "FAIL",
           viable ? "VIABLE" : "NOT VIABLE");
}
```

## Testing Your Implementation

The updated `main.c` includes a new test function called `test_bitmask_optimization` that tests your implementation. This function:

1. Creates test words and prints their masks
2. Generates feedback and converts it to a mask
3. Tests the pre-screening with various words
4. Compares the pre-screening results with the full `is_viable` check

The test function also includes a performance test with the dictionary:

```c
// Test with a larger set of words if the dictionary is available
FILE *word_file = fopen(WORD_LIST_FILENAME, "r");
if (word_file != NULL) {
    // ...

    printf("\nSummary for %zu words:\n", words_to_test);
    printf("  Words passing pre-screening: %d\n", prescreen_pass_count);
    printf("  Words passing full is_viable: %d\n", viable_count);
    printf("  Words passing both checks: %d\n", both_pass_count);
    printf("  Pre-screening efficiency: %.2f%%\n",
           (viable_count > 0) ?
           (float)both_pass_count / viable_count * 100.0 : 0.0);
}
```

This will show you how effective your optimization is at filtering out non-viable words.

## Debugging Tips

If your implementation doesn't work correctly, check:

1. Are you setting bits correctly in the word masks? Remember that bit positions start at 0 for 'a'.
2. Are you handling the upper 32 bits (exclusion bits) correctly in `feedback_to_mask`?
3. Is your pre-screening check `(word.mask & mask) == expected` implemented correctly?
4. Are you extracting the expected bits correctly using `mask & 0xFFFFFFFF`?

A common mistake is to forget to set both the lower and upper bits when initializing word masks, or to mix up which bits go where in the feedback mask.

## Wrapping Up

This optimization will significantly improve the performance of your Wordle helper, especially for large dictionaries. By using bit vectors, you've learned a powerful optimization technique that's widely used in many applications.

Congratulations on completing the entire Wordle helper project! You've built a sophisticated application that demonstrates many important concepts in C programming, including:

- Dynamic memory management
- Algorithmic optimization
- Bit manipulation
- File I/O
- Data structures
- Testing and debugging

Your implementation now efficiently helps players solve Wordle puzzles by suggesting optimal guesses based on rigorous analysis of the game's mechanics.


Compare the speed of you code from steps 3, 4, and 5.
