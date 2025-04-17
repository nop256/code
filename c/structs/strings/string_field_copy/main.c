#include <stdio.h>
#include <string.h>

struct person
{
	char name[20];
	int age;
};


int main(void)
{
	struct person p1 = {"Alice",30};
	struct person p2 = p1;
	strcpy(p2.name, "Bob");
	printf("Name 1: %s, Age: %d\n",p1.name, p1.age);
	printf("Name 2: %s, Age: %d\n",p2.name, p2.age);
}

