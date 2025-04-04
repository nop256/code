



long reversebits(unsigned long set){
	unsigned long out = 0;
	for (long i = 0; i < sizeof(set) * 8; i++){
		out <<= 1;
		out |= set & 1;
		set >>= 1;
	}
	return out;
}
