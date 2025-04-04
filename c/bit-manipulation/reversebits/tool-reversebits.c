#include <stdio.h>

void print_binary(unsigned x) {
    for (int i = sizeof(x) * 8 - 1; i >= 0; i--) {
        printf("%d", (x >> i) & 1);
        if (i % 4 == 0) printf(" "); 
    }
}

unsigned reversebits(unsigned x){
	unsigned out = 0;
	for (unsigned i = 0; i < sizeof(x) * 8; i++){
		out <<= 1;
		out |= x & 1;
		x >>= 1;
	}
	return out;
}


int main(void){
	unsigned x;
	printf("Enter an unsigned integer: ");
	scanf("%u", &x);

	printf("Your integer in binary:	   ");
	print_binary(x);
	printf("\n");

	unsigned reverse = reversebits(x);
	
	printf("Reversed in binary:	   ");
	print_binary(reverse);
	printf("\n");
	
	return 0;
}
