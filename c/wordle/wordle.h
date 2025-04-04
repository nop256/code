#ifndef WORDLE_H
#define WORDLE_H

#include <stdbool.h>
#include <stddef.h>

#define WORD_LENGTH 5
#define WORD_LIST_FILENAME "words.txt"

/* vector.c */
struct vector {
    char **array;
    size_t len;
    size_t cap;
};

struct vector *vector_new(void);
void vector_push(struct vector *v, char *word);
void vector_free(struct vector *v);


/* read_words.c */
struct vector *read_words(char *filename);


/* feedback.c */
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

// create a feedback by comparing a guess with the solution
struct feedback make_feedback(char *solution, char *guess);

// check if a word is still viable given a guess with feedback
bool is_viable(char *word, struct feedback feedback);

// parse a line of input into a feedback struct
// return true if valid
bool parse_feedback(char *input, struct feedback *feedback);


/* suggest.c */
/**
 * Struct representing a word and its expected score
 * The score is the expected number of words remaining after guessing this word
 */
struct word_score {
    char *word;        /* The suggested word */
    double score;      /* Expected number of words remaining (lower is better) */
};

/**
 * Struct containing a sorted array of word suggestions with their scores
 */
struct suggestion_list {
    struct word_score *suggestions; /* Array of suggestions (sorted by score) */
    size_t count;                   /* Number of suggestions in the array */
};

/**
 * Generate a sorted list of word suggestions based on their effectiveness
 * as Wordle guesses.
 *
 * For each word in the dictionary, this function:
 * 1. Tries the word as a guess against all possible solutions
 * 2. Calculates how many words would remain on average after that guess
 * 3. Returns words sorted by their effectiveness (lower average remaining is better)
 *
 * @param dictionary The dictionary of valid words (BORROWED: not modified, not freed)
 * @return A suggestion_list with words sorted by score (CALLER OWNS: caller must free with free_suggestions)
 */
struct suggestion_list generate_suggestions(struct vector *dictionary);

/**
 * Free memory associated with a suggestion list
 *
 * @param suggestions The suggestion list to free
 */
void free_suggestions(struct suggestion_list *suggestions);


/* ui.c */
/**
 * Run the interactive UI for the Wordle solver
 *
 * @param dictionary The dictionary of valid words
 * (OWNERSHIP TRANSFERRED: this function will free the dictionary when done)
 */
void consume_dictionary_and_run_ui(struct vector *dictionary);

#endif /* WORDLE_H */
