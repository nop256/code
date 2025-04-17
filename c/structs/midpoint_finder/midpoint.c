#include <stdio.h>

struct Point
{
	int x;
	int y;
};

struct Line
{
	struct Point p1;
	struct Point p2;
};

struct Line reflect_line(struct Line *l)
{
	l->p1.x = -l->p1.x;	
	l->p1.y = -l->p1.y;
	l->p2.x = -l->p2.x;
	l->p2.y = -l->p2.y;
	return *l;
}

struct Point midpoint(struct Line l)
{
	struct Point mid;
	mid.x = (l.p1.x + l.p2.x) / 2;
	mid.y = (l.p1.y + l.p2.y) / 2;
	return mid;
}

int slope(struct Line *l)
{
	int m = ((l->p2.y - l->p1.y) / (l->p2.x - l->p1.x));
	return m;
}

int main(void)
{
	struct Line l1 = {{2,2}, {4,28}};
	struct Point mid1 = midpoint(l1);
	int slope1 = slope(&l1);
	printf("Original line: {{%d,%d},{%d,%d}}\n",l1.p1.x,l1.p1.y,l1.p2.x,l1.p2.y);
	printf("Original Midpoint: (%d, %d)\n",mid1.x,mid1.y);
	printf("Original Slope: %d\n", slope1);
	reflect_line(&l1);
	int slope2 = slope(&l1);
	struct Point mid2 = midpoint(l1);
	printf("Reflected line: {{%d,%d},{%d,%d}}\n",l1.p1.x,l1.p1.y,l1.p2.x,l1.p2.y);
	printf("Reflected Midpoint: (%d, %d)\n",mid2.x,mid2.y);
	printf("Reflected Slope: %d\n", slope2);
}
