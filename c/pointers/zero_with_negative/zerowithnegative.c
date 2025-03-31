#include <stdio.h>


int replacezero(int *elt){
    if (*elt == 0){
        *elt = -1;
        return 1;
    } return 0; 
}

int fixzeros(int *lst, int len){
    int count = 0;
    for (int i = 0; i<len; i++){
        count += replacezero(&lst[i]);
    } return count; 
}

void printarray(int *arr, int len){
    printf("[");
    for (int i=0; i<len; i++){
        printf("%d", arr[i]);
        if (i<len-1) printf(", ");
    } printf("]\n");
}

int main(void){
    int arr[]={0,4,0,5,6,0};
    int count = fixzeros(arr, 6);
    printarray(arr, 6);
    printf("Values modified: %d\n", count);
}

