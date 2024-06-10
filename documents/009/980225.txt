#include <stdio.h>
#include <string.h>

void reverse(char str[]) {
  int i, j;
  char ch;
  int length = strlen(str);

  for (i = 0, j = length - 1; i < j; i++, j--) {
    ch = str[i];
    str[i] = str[j];
    str[j] = ch;
  }
}

int main(void)
{
  char str[20 + 1];

  scanf("%s", str);
  reverse(str);
  printf("%s\n", str);

  return 0;
}