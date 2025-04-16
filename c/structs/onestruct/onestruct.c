#include <stdio.h>

int main(void){
	struct Point {
		int x;
		int y;
	};
	
	struct Point p1 = {2, 3};
	printf("%d %d\n", p1.x, p1.y);
}
