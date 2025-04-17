#include <stdio.h>

struct Point
{
	int x;
	int y;
};

struct Point reflect_over_x(struct Point p)
{
	p.y = -p.y;
	return p;
}

int main(void)
{
	struct Point pt = {2, -5};
	printf("Before reflect: %d %d\n",pt.x,pt.y);
	struct Point ptr = reflect_over_x(pt);
	printf("After reflect: %d %d\n",ptr.x,ptr.y);
}
