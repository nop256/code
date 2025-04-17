#include <stdio.h>
#include <string.h>

struct Point
{
	int x;
	int y;
};

struct Triangle
{
	struct Point a;
	struct Point b;
	struct Point c;
};

int isright(struct Triangle t)
{
	/** OLD
	int dx = t.b.x - t.a.x;
	int dy = t.b.y - t.a.y;
	int dz = t.c.x - t.b.x;
	int dist1 = dx * dx + dy * dy; 
	if (dist1 == (dz * dz))
	{
		return 1;
	} else {
		return 0;
	}
	**/
	// NEW
	int ab2 = (t.a.x - t.b.x)*(t.a.x - t.b.x) + (t.a.y - t.b.y)*(t.a.y - t.b.y);
	int bc2 = (t.b.x - t.c.x)*(t.b.x - t.c.x) + (t.b.y - t.c.y)*(t.b.y - t.c.y);
	int ca2 = (t.c.x - t.a.x)*(t.c.x - t.a.x) + (t.c.y - t.a.y)*(t.c.y - t.a.y);
	return (ab2 + bc2 == ca2 ||
			ab2 + ca2 == bc2 ||
			bc2 + ca2 == ab2);
}

int main(void)
{
	struct Triangle r = {{0,0},{3,0},{0,4}};
	struct Triangle nr = {{1,1},{2,2},{3,3}};
	//char str1[20];
	//char str2[20];
	const char *str1;
	const char *str2;

	if (isright(r))
	{
		//strcpy(str1, "is");
		str1 = "is";
	} else {
		//strcpy(str1, "is not");
		str1 = "is not";
	}
	if (isright(nr))
	{
		//strcpy(str2, "is");
		str2 = "is";
	} else {
		//strcpy(str2, "is not");
		str2 = "is not";
	}
	printf("Triangle 1 %s a right triangle.\n",str1);
	printf("Triangle 2 %s a right triangle.\n",str2);
}
