#include <stdio.h>
#include<stdlib.h>
#include<string.h>

struct book {
  char name[30];
  char author[30];
  int year;
};

int main()
{
  printf("Size of book is %lu\n", sizeof(struct book));
  struct book* harry_potter = malloc(sizeof(struct book));
  harry_potter->year = 1998;
  printf("Data wydania książki to %d\n", harry_potter->year);
  strcpy(harry_potter->author, "J.K. Rowling");

  printf("Autor książki to %s\n", harry_potter->author);
  /* (*(*(*a).b).c) */
  /* a->b->c */
  return 0;
}
