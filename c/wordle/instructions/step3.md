# Wordle solver step 3

In this third step, you'll implement a suggestion system that analyzes the effectiveness of different word guesses in the Wordle game.

## Learning Objectives

- Implement a statistical analysis algorithm
- Work with nested data structures
- Sort complex objects with `qsort` in C
- Manage memory for more complex data structures

## Project Overview

Building on your vector and feedback implementations from Steps 1 and 2, you'll now add:

1. A function to evaluate word guesses by calculating how many words would remain viable after each guess
2. A function to generate a sorted list of suggestions, ranked by effectiveness
3. A memory management function to free the suggestion structures

## Files Description

- `main.c`: Test program (provided)
- `wordle.h`: Updated header file with all definitions (provided)
- `ui.c`: Interactive UI for the Wordle solver (provided)
- `suggest.c`: Implement your suggestion functions here

## Implementation Tasks

### 1. Suggestion System Implementation

Implement these functions in `suggest.c`:

#### `struct suggestion_list generate_suggestions(struct vector *dictionary)`

Generates a sorted list of word suggestions based on their effectiveness:

- For each word in the dictionary:
  - Calculate how effective it would be as a guess by simulating it against all possible solutions
  - Compute the average number of words that would remain viable after this guess
  - Add the word and its score to the suggestion list
- Sort the list by score (lower scores are better)
- Return the completed suggestion list

Detailed approach:
1. Create a suggestion list large enough to hold all dictionary words
2. For each potential guess word:
   - For each possible solution word:
     - Use `make_feedback` to get feedback for this guess against this solution
     - Count how many words in the dictionary would remain viable given this feedback using `is_viable`
   - Calculate the average number of remaining words across all solutions
   - Create a copy of the word and store it with its score
3. Sort all word-score pairs using `qsort` (lower average is better)
4. Return the suggestion list

#### `void free_suggestions(struct suggestion_list *suggestions)`

Frees all memory associated with a suggestion list:

- Free each word string in the suggestions array
- Free the suggestions array itself
- Reset the count to 0

### 2. Suggestion Sorting

For sorting the suggestions, you'll need to implement a comparison function for `qsort`:

```c
static int compare_word_scores(const void *a, const void *b) {
    const struct word_score *score_a = (const struct word_score *)a;
    const struct word_score *score_b = (const struct word_score *)b;

    /* Sort by score (ascending - lower is better) */
    if (score_a->score < score_b->score) return -1;
    if (score_a->score > score_b->score) return 1;

    /* If scores are equal, sort alphabetically */
    return strcmp(score_a->word, score_b->word);
}


Before you move on to step 4, you may wish to make a copy of this
code. The next steps will be optmizing this code to run faster, so
keep a copy of this version to test against.

To get a timing measurement, run:

    echo | time make run

If you want to compare the longer and shorter dictionaries, both are
provided here as "long.txt" and "short.txt" (words.txt is the same
as short.txt by default). Copy one of these over top of words.txt
and compare the timing and output.
