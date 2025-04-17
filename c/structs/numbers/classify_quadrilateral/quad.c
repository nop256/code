#include <stdio.h>
#include <math.h>

struct point
{
	int x;
	int y;
};

struct quad
{
	struct point a;
	struct point b;
	struct point c;
	struct point d;
};

int isrectangle(struct quad q)
{
	int AB = sqrt(pow((q.b.x - q.a.x),2)+pow((q.b.y - q.a.y),2));
	int BC = sqrt(pow((q.c.x - q.b.x),2)+pow((q.c.y - q.b.y),2));
	int CD = sqrt(pow((q.d.x - q.c.x),2)+pow((q.d.y - q.c.y),2));
	int DA = sqrt(pow((q.a.x - q.d.x),2)+pow((q.a.y - q.d.y),2));
	return (AB == CD &&
			BC == DA);
}

int main(void)
{
	struct quad r = {{0, 0}, {4, 0}, {4, 3}, {0, 3}};
	struct quad nr = {{1, 1}, {3, 1}, {3, 2}, {2, 2}};
	const char *str1;
	const char *str2;

	if (isrectangle(r)) str1 = "is";
	else if (!isrectangle(r)) str1 = "is not";

	if (isrectangle(nr)) str2 = "is";
	else if (!isrectangle(nr)) str2 = "is not";

	printf("Quadrilateral 1 %s a rectangle\n", str1);
	printf("Quadrilateral 2 %s a rectangle\n", str2);
}
