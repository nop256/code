

#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_N 10000
void sieve(bool *array, int size){
    // initialize all elements to true
    for (int i=0; i<size; i++) array[i]=true;

    // start outer loop at 2, stop at sqrt(size)
    for (int i=2; i*i < size; i++){
        // if number is prime (true), then process its multiples
        if (array[i]) {
            for (int j= i+i; j<size; j+=i){
                array[j]=false;
            }
        }
    }
}
















/*
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
*/
