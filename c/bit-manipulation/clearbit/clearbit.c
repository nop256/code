#include <stdio.h>

void clear_bit(unsigned *set, int n){
	*set &= ~(1 << n);
}
