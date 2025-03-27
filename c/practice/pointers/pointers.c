

#include <stdio.h>

int main(void){
    int x = 10;
    int *p = &x;
    printf("x = %d\n", x);
    printf("p = %p\n", p);
    printf("*p = %d\n", *p);
    printf("&x = %p\n", &p);
}
