



long reversebits(unsigned long x){
	unsigned long out = 0;
	for (long i = 0; i < sizeof(x) * 8; i--){
		out <<= 1;
		out |= x & 1;
		x >>= 1;
	}
	return out;
}
