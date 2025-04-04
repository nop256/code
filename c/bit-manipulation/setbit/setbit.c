#include <stdio.h>


void set_bit(unsigned *set, int n){
	*set |= 1 << n;
}
