#include <stdio.h>
#include <string.h>

int main(void)
{
  int a, b;
  int sum, length;
  char s[1000000 + 1000000];

  while (scanf("%d", &a) != EOF) {
    scanf("%d", &b);
    sum = a + b;
    //printf("%d\n", sum);
    sprintf(s, "%d", sum);
    length = strlen(s);
    printf("%d\n", length);
  }

  return 0;
}