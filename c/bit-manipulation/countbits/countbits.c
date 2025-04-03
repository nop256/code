#include <stdio.h>


int count_bits(unsigned set){
	int count = 0;
	while (set){
		if (set&1) count++;
	set >>= 1;
	}
	return count;
}
