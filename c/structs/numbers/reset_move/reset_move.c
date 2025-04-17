#include <stdio.h>

struct Point {
	int x;
	int y;
};

void reset_point(struct Point p){
	p.x = 0;
	p.y = 0;
}

void move_point(struct Point *p, int dx, int dy){
	 p->x += dx;
	 p->y += dy;
}

int main(void){
	struct Point pt = {5, 10};
	reset_point(pt);
	printf("%d %d\n", pt.x, pt.y);
	move_point(&pt, -2, 3);
	printf("%d %d\n", pt.x, pt.y);
}
