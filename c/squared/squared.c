/* write 2 functions, one of which calls the other. 
 * The first one replaces the number pointed to by elt with its square
 * prototype:   void modify(int *elt);
 *
 * The second loops over the 'len' elements in lst, and for each one, calls the helper function to modify that element
 * prototype:   void apply_to_array(int *lst, int len);
 */

#include <stdio.h>

void modify(int *elt){
    *elt *= *elt;
}

void apply_to_array(int *lst, int len){
    for (int i=0; i<len; i++){
        printf("Before: i = %d, lst[i] = %d, &lst[i] = %p\n", i, lst[i], (void*)&lst[i]);
        
        modify(&lst[i]);

        printf("After: i = %d, lst[i] = %d, &lst[i] = %p\n", i, lst[i], (void*)&lst[i]);
    }
}

void print_array(int *arr, int len) {

int main(void){
    int arr[] = {1,2,3,4};
    int len = sizeof(arr);
    apply_to_array(arr, 4);
    printf("\n");
    for (int i=0; i<4; i++){
        printf("%d", arr[i]);
    }
    printf("\n");
    printf("sizeof(arr) = %d", len); 
    return 0;
}
