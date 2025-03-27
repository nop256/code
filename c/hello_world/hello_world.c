#include <stdio.h>
#include <string.h>

int main(void){
    char greeting[] = "hello world!";
    int len = strlen(greeting);
    for (int i=0; i < len; i++){
        printf("%c\n", greeting[i]);
                }
    puts(greeting);
    }
