#include <stdio.h>

unsigned reverse(unsigned x){
	unsigned out = 0;
	for (unsigned i = 0; i < sizeof(x)*8; i++){
		out <<= 1;
		out |= x & 1;
		x >>= 1;
	}
	return out;
}

unsigned checkset(unsigned x, int index){
	return (x >> index) & 1;
}

int countbits(unsigned x){
	int count = 0;
	while (x){
		x &= (x-1);
		count++;
	}
	return count;
}

int revtool(unsigned x, int index){
	unsigned rx = reverse(x);
	rx |= 1 << index;
	rx &= ~(1 << (index+1));
	if (checkset(rx, (index+2))){\
		printf("Bit at index %d is ON", (index+2));
	} else {
		printf("bit at index %d is OFF", (index+2));
	}
	return countbits(rx);
}

int main(void) {
    unsigned x = 0b00011100;
    int index = 2;

    int count = revtool(x, index);
    printf("\nLive bit count: %d\n", count);
    return 0;
}
