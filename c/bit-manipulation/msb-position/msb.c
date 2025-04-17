



int msbpos(unsigned x){
	int count = 0;
	while (x){
		count++;
		x &= (x-1);
	}
	return count;
}
