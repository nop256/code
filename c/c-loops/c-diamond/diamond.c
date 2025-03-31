#include <stdio.h>

void print_diamond(int size){
    int spaces=size-1;
    int stars=1;

    //top half
    for (int i=0;i<size;i++){
        for (int sp=0; sp<spaces; sp++){
            putchar(' ');
        }
        for (int st=0; st<stars; st++){
            putchar('*');
        }
        putchar('\n');
        spaces--;
        stars+=2;
    }

    //bot half
    spaces=1;
    stars-=4;
    for (int i=0; i<size-1; i++){
        for (int sp=0; sp<spaces; sp++){
            putchar(' ');
        }
        for (int st=0; st<stars; st++){
            putchar('*');
        }
        putchar('\n');
        spaces++;
        stars-=2;
    }
}

