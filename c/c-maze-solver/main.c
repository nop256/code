#include <stdio.h>
#include <string.h>
#include "solve.h"

int main(void) {
    char field[SIZE_Y][SIZE_X];

    // read the maze in from standard in
    char line[SIZE_X+2];
    for (int y = 0; y < SIZE_Y; y++) {
        if (fgets(line, SIZE_X+2, stdin) == NULL) {
            printf("error reading line %d\n", y+1);
            return 0;
        }
        if (strlen(line) != SIZE_X+1) {
            printf("line %d was the wrong length\n", y+1);
            return 0;
        }
        for (int x = 0; x < SIZE_X; x++)
            field[y][x] = line[x];
    }

    // print the field
    printf("the original maze:\n");
    print_maze(field);
    fflush(stdout);

    return 0;
}
