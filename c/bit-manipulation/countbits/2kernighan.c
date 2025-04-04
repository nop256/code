



int countbits(unsigned set, int n){
	int count = 0;
	while (set){
		set &= (set-1);
		count++;
	}
	return count;
}
