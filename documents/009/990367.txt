#include <stdio.h>

int main(void)
{
  short a, b, c, n;
  char i;

  scanf("%hd", &n);

  for (i = 0; i < n; i++) {
    scanf("%hd%hd%hd", &a, &b, &c);
    if (a*a+b*b == c*c || a*a+c*c == b*b || b*b+c*c == a*a)
      printf("YES\n");
    else
      printf("NO\n");
  }

  return 0;
}