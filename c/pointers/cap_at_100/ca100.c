#include <stdio.h>


int cap_at_100(int *elt){
    if (*elt > 100){
        *elt = 100;
        return 1;
    }
    return 0;
}

int normalize_array(int *lst, int len){
    int count = 0;
    for (int i=0; i<len; i++) count += cap_at_100(&lst[i]);
    return count;
}

void print_array(int *arr, int len){
    printf("[");
    for (int i=0; i<len; i++){
        printf("%d",arr[i]);
        if (i < len-1) printf(", ");
    }
    printf("]");
}

int main(void){
    int arr[]={-1,9,23,127,0,286,69,6969,696};
    int count = normalize_array(arr, 9);
    print_array(arr, 9);
    printf("\nValues modified: %d\n", count);
    return 0;
}



