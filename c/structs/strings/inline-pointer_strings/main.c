#include <stdio.h>
#include <string.h>


struct person
{
	char name[20];			//inline string - deep copy
	const char *nickname;	//pointer string - shallow copy
	int age;
};

int main(void)
{
	struct person p1 = {"Alice","Ally",30};
	struct person p2 = p1;
	strcpy(p2.name,"Bob");
	p2.nickname = "Bobby";
	printf("Person 1 - Name: %s, Nick: %s, Age: %d\n",p1.name,p1.nickname,p1.age);
	printf("Person 2 - Name: %s, Nick: %s, Age: %d\n",p2.name,p2.nickname,p2.age);
}
