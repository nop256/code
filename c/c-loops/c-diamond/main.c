#include <stdio.h>

void print_diamond(int);

int main(void) {
    /* turn off stdout buffering */
    setbuf(stdout, NULL);

    int size;
    char *newline = "";
    while (scanf("%d", &size) == 1) {
        printf("%s", newline);
        newline = "\n";

        print_diamond(size);
        fflush(stdout);
    }

    return 0;
}
