#include <stdio.h>


int triple_if_multiple_of_three(int *elt){
    if (*elt % 3 == 0) {
        *elt *= 3;
        return 1;
    } else {
        return 0;
    }
}

int boost_array(int *lst, int len){
    int count = 0;
    for (int i=0; i<len; i++){
        count += triple_if_multiple_of_three(&lst[i]);
    }
    return count;
}

void print_array(int *arr, int len){
    printf("[");
    for (int i=0; i<len;i++){
        printf("%d", arr[i]);
        if (i<len-1) printf(",");
    }
    printf("]\n");
}

int main(void){
    int arr[]={1,2,3,6,9,12,10,8};
    int count = boost_array(arr, 8);
    print_array(arr, 8);
    printf("\nValues modified: %d\n", count);
    return 0;
}
