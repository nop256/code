



unsigned char reversebit(unsigned char x){
	unsigned char out = 0;
	for (unsigned char i = 0; i < sizeof(x) * 8; i++){
		out <<= 1;
		out |= x & 1;
		x >>= 1;
	}
	return out;
}





