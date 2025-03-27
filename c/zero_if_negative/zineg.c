#include <stdio.h>

int zero_if_negative(int *elt){
    if (*elt < 0){
        *elt = 0;
        return 1;
    } else {
        return 0;
    }
}

int sanitize_array(int *lst, int len){
    int count = 0;
    for (int i=0; i<len; i++){
        count += zero_if_negative(&lst[i]);
    }
    return count;
}

void print_array(int *arr, int len){
    printf("[");
    for (int i=0; i<len; i++){
        printf("%d", arr[i]);
        if (i<len-1) printf(",");
    }
    printf("]\n");
}

int main(void){
    int arr[] = {1,-2,12,-5,6,6,-3};
    int count = sanitize_array(arr, 7);
    print_array(arr, 7);
    printf("Number of changes: %d\n", count);
}
