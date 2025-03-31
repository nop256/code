/*
 * Write 2 functions, one of which calls the other.
 *
 * The first function should check whether the number pointed to by 'elt' is even.
 * If it is even, replace it with 0.
 * If it is odd, leave it unchanged.
 * 
 * Prototype: void zero_if_even(int *elt);
 *
 * The second function should loop over the 'len' elements in lst, and for each one,
 * call the helper function to conditionally modify that element.
 *
 * Prototype: void process_array(int *lst, int len);
 *
 * Then, in main, define an array of ints, pass it to your process_array function,
 * and print out the modified array in a [1, 2, 3] format.
 */

#include <stdio.h>


void zero_if_even(int *elt){
    if (*elt % 2 == 0) *elt = 0;
}

void process_array(int *lst, int len){
    for (int i=0; i<len; i++) zero_if_even(&lst[i]);
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
    int arr[] = {1,2,3,4,5,6};
    process_array(arr, 6);
    print_array(arr, 6);
}
