#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_N 10000
void sieve(bool *array, int size);

int main(void) {
    // allocate an array of bools
    bool *list = malloc(MAX_N * sizeof(bool));
    if (list == NULL) {
        perror("malloc");
        exit(1);
    }

    // call the sieve function
    sieve(list, MAX_N);

    // print the results
    char *space = "";
    for (int i = 2; i < MAX_N; i++) {
        if (list[i]) {
            printf("%s%d", space, i);
            space = " ";
        }
    }
    printf("\n");

    // free the array
    free(list);

    return 0;
}
