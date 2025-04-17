#include <stdio.h>
#include <string.h>

struct Person
{
    char name[20];
    const char *nick;
    int age;
};

struct People
{
    struct Person a;
    struct Person b;
    struct Person c;
};

void updatename(struct Person *p, const char *newname)
{
    strcpy(p->name,newname);
}

void updateperson(struct Person *p, const char *newname, const char *newnick, int newage)
{
    strcpy(p->name,newname);
    p->nick = newnick;
    p->age = newage;
}



int main(void)
{
    struct People p1 = {{"Alfred", "Alf", 50},
                        {"Bernard", "Barry", 36},
                        {"Charles", "Charlie", 28}};
    printf("Person 1 Name: %s, Nickname: %s, Age: %d\n", p1.a.name, p1.a.nick, p1.a.age);
    printf("Person 2 Name: %s, Nickname: %s, Age: %d\n", p1.b.name, p1.b.nick, p1.b.age);
    printf("Person 3 Name: %s, Nickname: %s, Age: %d\n", p1.c.name, p1.c.nick, p1.c.age);
    updatename(&p1.a,"Al");
    printf("Person 1 New Name: %s, Nickname: %s, Age: %d\n", p1.a.name, p1.a.nick, p1.a.age);
    updateperson(&p1.b,"Bravo","Brav",88);
    printf("New Person 2 Name: %s, Nickname: %s, Age: %d\n", p1.b.name, p1.b.nick, p1.b.age);
};
