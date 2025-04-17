#include <stdio.h>

struct Point {
	int x;
	int y;
};

void swap_coords(struct Point *p){
	int temp = p->x;
	p->x = p->y;
	p->y = temp;
}

struct Point make_point(int x, int y){
	struct Point p1 = {x, y};
	return p1;
}

int main(void){
	struct Point pt = make_point(7,3);
	printf("Before swap: %d %d\n", pt.x, pt.y);
	swap_coords(&pt);
	printf("After swap: %d %d\n", pt.x, pt.y);
}
