



int isbitset(unsigned *set, int n){
	return (*set >> n) & 1;
}
