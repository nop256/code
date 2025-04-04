#include <stdio.h>
#include <stdlib.h>
#include "wordle.h"

void test_vector_new(void);
void test_vector_push(void);
void test_vector_free(void);
void test_read_words(void);

int main(void) {
    printf("=== Testing Wordle Helper Step 1 ===\n\n");

    // Run all tests in sequence
    test_vector_new();
    printf("\n");

    test_vector_push();
    printf("\n");

    test_vector_free();
    printf("\n");

    test_read_words();

    return 0;
}

// Test vector_new function
void test_vector_new(void) {
    printf("=== Testing vector_new() ===\n");

    struct vector *v = vector_new();
    printf("New vector created:\n");
    printf("  capacity: %zu\n", v->cap);
    printf("  length: %zu\n", v->len);

    // Write to first and last elements of the array to test bounds
    // This will cause valgrind to detect errors if allocation is too small
    if (v->cap > 0) {
        v->array[0] = NULL;
        v->array[v->cap - 1] = NULL;
        printf("  Successfully accessed first and last array elements\n");
    }

    // Clean up - we'll test vector_free separately
    for (size_t i = 0; i < v->len; i++) {
        free(v->array[i]);
    }
    free(v->array);
    free(v);

    printf("Test completed.\n");
}

// Test vector_push function
void test_vector_push(void) {
    printf("=== Testing vector_push() ===\n");

    // Create a vector
    struct vector *v = vector_new();
    printf("New vector created with capacity: %zu, length: %zu\n", v->cap, v->len);

    // Test adding a single string
    printf("\nAdding string \"hello\"...\n");
    vector_push(v, "hello");
    printf("After first push:\n");
    printf("  capacity: %zu\n", v->cap);
    printf("  length: %zu\n", v->len);
    printf("  first element: %s\n", v->array[0]);

    // Test adding another string
    printf("\nAdding string \"world\"...\n");
    vector_push(v, "world");
    printf("After second push:\n");
    printf("  capacity: %zu\n", v->cap);
    printf("  length: %zu\n", v->len);
    printf("  first element: %s\n", v->array[0]);
    printf("  second element: %s\n", v->array[1]);

    // Test expansion by adding many strings
    printf("\nTesting capacity expansion...\n");
    size_t initial_cap = v->cap;
    size_t strings_to_add = initial_cap * 2;

    printf("Adding %zu more strings...\n", strings_to_add);
    for (size_t i = 0; i < strings_to_add; i++) {
        char buffer[20];
        sprintf(buffer, "test%zu", i);
        vector_push(v, buffer);
    }

    printf("After adding many strings:\n");
    printf("  capacity: %zu\n", v->cap);
    printf("  length: %zu\n", v->len);
    printf("  last element: %s\n", v->array[v->len - 1]);

    // Clean up
    for (size_t i = 0; i < v->len; i++) {
        free(v->array[i]);
    }
    free(v->array);
    free(v);

    printf("Test completed.\n");
}

// Test vector_free function
void test_vector_free(void) {
    printf("=== Testing vector_free() ===\n");

    // Create a vector
    struct vector *v = vector_new();

    // Add some strings
    vector_push(v, "test");
    vector_push(v, "vector");
    vector_push(v, "free");

    printf("Created vector with %zu elements\n", v->len);
    printf("Calling vector_free()...\n");

    // Test vector_free
    vector_free(v);

    printf("Vector freed successfully\n");
    printf("Test completed.\n");
}

// Test read_words function
void test_read_words(void) {
    printf("=== Testing read_words() ===\n");

    // Create a test file with some words
    printf("Creating test file 'test_words.txt'...\n");
    FILE *test_file = fopen("test_words.txt", "w");
    if (test_file == NULL) {
        fprintf(stderr, "Could not create test file\n");
        return;
    }

    // Write some test words - mix of valid and invalid
    fprintf(test_file, "hello\n");   // valid
    fprintf(test_file, "world\n");   // valid
    fprintf(test_file, "apple\n");   // valid
    fprintf(test_file, "grape\n");   // valid
    fprintf(test_file, "pear\n");    // invalid (4 letters)
    fprintf(test_file, "orange\n");  // invalid (6 letters)
    fprintf(test_file, "UPPER\n");   // invalid (uppercase)
    fprintf(test_file, "mix3d\n");   // invalid (contains digit)
    fclose(test_file);

    printf("Reading words from test file...\n");
    struct vector *words = read_words("test_words.txt");

    printf("Read %zu words\n", words->len);
    printf("Words found (should only include valid 5-letter lowercase words):\n");
    for (size_t i = 0; i < words->len; i++) {
        printf("  Word %zu: %s\n", i, words->array[i]);
    }

    vector_free(words);

    // Remove the test file when done
    remove("test_words.txt");
    printf("Test file removed\n");

    // Test with actual word list if available
    FILE *word_file = fopen(WORD_LIST_FILENAME, "r");
    if (word_file != NULL) {
        fclose(word_file);

        printf("\nTesting with actual word list '%s'...\n", WORD_LIST_FILENAME);
        struct vector *full_words = read_words(WORD_LIST_FILENAME);

        printf("Read %zu words from %s\n", full_words->len, WORD_LIST_FILENAME);

        // Print a sample of words
        printf("Sample of first few words:\n");
        size_t sample_size = 5;
        if (full_words->len < sample_size) {
            sample_size = full_words->len;
        }

        for (size_t i = 0; i < sample_size; i++) {
            printf("  Word %zu: %s\n", i, full_words->array[i]);
        }

        // Print every 100th word
        printf("\nEvery 100th word:\n");
        for (size_t i = 0; i < full_words->len; i += 100) {
            if (i < full_words->len) {
                printf("  Word %zu: %s\n", i, full_words->array[i]);
            }
        }

        // Print last word
        if (full_words->len > 0) {
            size_t last = full_words->len - 1;
            printf("\nLast word (%zu): %s\n", last, full_words->array[last]);
        }

        vector_free(full_words);
    } else {
        printf("\nFile '%s' not found. Skipping full word list test.\n", WORD_LIST_FILENAME);
    }

    printf("Test completed.\n");
}
