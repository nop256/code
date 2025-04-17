#include <stdio.h>
#include <string.h>


struct person
{
	char name[20];
	const char *nick;
	int age;
};

void updatename(struct person *p, const char *newname)
{
	strcpy(p->name, newname);
}

void updatenick(struct person *p, const char *newnick)
{
	p->nick = newnick;
}

void updateage(struct person *p, int newage)
{
	p->age = newage;
}

void updateperson(struct person *p, const char *newname, const char *newnick, int newage)
{
	strcpy(p->name, newname);
	p->nick = newnick;
	p->age = newage;
}

int main(void)
{
	struct person p1 = {"Alice", "Ally", 30};
	printf("Original Name: %s, Nick: %s, Age: %d\n",p1.name,p1.nick,p1.age);
	updatename(&p1, "Bob");
	printf("Updated Name: %s, Nick: %s, Age: %d\n",p1.name,p1.nick,p1.age);
	updatenick(&p1, "Bobby");
	printf("Updated Nick: %s, Nick: %s, Age: %d\n",p1.name,p1.nick,p1.age);
	updateage(&p1, 69);
	printf("Updated Age: %s, Nick: %s, Age: %d\n",p1.name,p1.nick,p1.age);
	updateperson(&p1, "Richard", "Dick", 108);
	printf("Updated Person: %s, Nick: %s, Age: %d\n",p1.name,p1.nick,p1.age);
}
