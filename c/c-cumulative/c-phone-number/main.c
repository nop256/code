#include <stdio.h>
#include <stdlib.h>
#include "phonenumber.h"

#define MAXLINE 100

int main(void) {
    char line[MAXLINE];

    while (fgets(line, MAXLINE, stdin) != NULL) {
        format_phone_number(line);
        fflush(stdout);
    }

    return 0;
}
