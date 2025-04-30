#include <stdio.h>
#include <stdlib.h>
#include "letters.h"

#define MAXLINE 1000

int main(void) {
    char line[MAXLINE];

    while (fgets(line, MAXLINE, stdin) != NULL) {
        letters_used(line);
        fflush(stdout);
    }

    return 0;
}
