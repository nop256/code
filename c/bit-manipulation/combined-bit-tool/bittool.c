#include <stdio.h>


int bit_tool(unsigned x, int index){
	x |= 1 << index;						// Set bit at index
	x &= ~(1 << (index+1));					// Clear bit at index+1

	if ((x >> (index+2)) & 1)				// Check bit at index+2
		printf("bit %d is ON.\n", index+2);
	else 
		printf("bit %d is OFF.\n", index+2);
	int count = 0;
	while (x){								//Kernighan's Algorithm
		x &= (x-1);
		count++;
	}
	printf("Live bits = %d\n", count);
	return count;
}

void print_binary(unsigned x){
	for (int i = sizeof(x) * 8 - 1; i >= 0; i--){
		printf("%d", (x>>i) &1);
		if (i%4==0) printf(" ");	// Group by 4 bits
	}
	printf("\n");
}

int main(){
	unsigned x;			// Allocate memory space to store unsigned int
	int index;			// Allocate memory space to store an int

	printf("Enter an unsigned integer value (decimal): ");
	scanf("%u", &x);	// Scan formatted input, %u data type specifier, store in memory address of x
	print_binary(x);

	printf("\nEnter a bit index to operate on: ");
	scanf("%d", &index);// Scan formatted input, %d data type specifier, store in memory address of index

	printf("\nPerforming bit operations on %u at inded %d...\n\n",x, index);

	bit_tool(x, index);

	return 0;
}
