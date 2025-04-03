#include <stdio.h>


int bit_tool(unsigned x, int index){
	x |= 1 << index;						// Set bit at index
	x &= ~(1 << (index+1));					// Clear bit at index+1

	if ((x >> (index+2)) & 1)				// Check bit at index+2
		printf("bit %d is ON.\n", index+2);
	else 
		printf("bit %d is OFF.\n", index+2);
	int count = 0;
	while (x){
		x &= (x-1);
		count++;
	}
	printf("Live bits = %d\n", count);
	return count;
}

int main(){
}
