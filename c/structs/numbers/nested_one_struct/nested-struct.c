#include <stdio.h>


struct Point
{
	int x;
	int y;
};

struct Box
{
	struct Point tl;
	struct Point br;
};

void move_box(struct Box *b, int dx, int dy)
{
	b->tl.x += dx;
	b->tl.y += dy;
	b->br.x += dx;
	b->br.y += dy;
}

struct Box make_box(int x1, int y1, int x2, int y2)
{
	struct Box box1 = {{x1, y1}, {x2, y2}};
	return box1;
}

int main(void)
{
	struct Box bx = make_box(0,0,5,5);
	printf("Before move: {{%d, %d}, {%d, %d}}\n",bx.tl.x, bx.tl.y, bx.br.x, bx.br.y);
	move_box(&bx, 3, -2);
	printf("After move: {{%d, %d}, {%d, %d}}\n",bx.tl.x, bx.tl.y, bx.br.x, bx.br.y);
}
