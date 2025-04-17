#include <stdio.h>


struct person
{
	const char *name;
	int age;
};


int main(void)
{
	struct person p1 = {"Alice", 30};
	struct person p2 = p1;
	p2.name = "Bob";
	printf("Person 1: %s, Age: %d\n",p1.name,p1.age);
	printf("Person 2: %s, Age: %d\n",p2.name,p2.age);
}
