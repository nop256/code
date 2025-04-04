#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "wordle.h"

#define MAX_LINE_LENGTH 8

// check that a word is 5 lower-case letters
static bool is_valid_word(char *word) {
    size_t len = strlen(word);

    // check length
    if (len != WORD_LENGTH) {
        return false;
    }

    // check that all characters are lowercase letters
    for (size_t i = 0; i < len; i++) {
        char letter = word[i];
        if (letter < 'a' || letter > 'z')
            return false;
    }

    return true;
}

struct vector *read_words(char *filename) {
    fprintf(stderr, "read_words: not implemented\n");
    exit(1);
}
