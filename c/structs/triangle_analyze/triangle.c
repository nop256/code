#include <stdio.h>

struct Point {int x; int y;};
struct Triangle {struct Point a; struct Point b; struct Point c;};

float slope(struct Point p1, struct Point p2)
{
	if (p2.x == p1.x) return 999999.0f;
	float m = (float)(p2.y - p1.y) / (p2.x - p1.x);
	printf("y2:%d, y1:%d, x2:%d, x1:%d\n", p2.y, p1.y, p2.x, p1.x);
	printf("Slope: %f\n",m);
	return m;
}

int main(void)
{
	struct Triangle t= {{0,0},{4,0},{2,3}};
	printf("Struct: {{%d,%d},{%d,%d},{%d,%d}}\n", t.a.x, t.a.y, t.b.x, t.b.y, t.c.x, t.c.y);
	float AB = slope(t.a,t.b);
	float BC = slope(t.b,t.c);
	float CA = slope(t.c,t.a);
	printf("Slope AB: %f\n",AB);
	printf("Slope BC: %f\n",BC);
	printf("Slope CA: %f\n",CA);
}

