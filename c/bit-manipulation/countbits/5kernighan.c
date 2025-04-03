



int countbits(unsigned x){
	int count = 0;
	while (x){
		x &= (x-1);
		count++;
	}
	return count;
}
