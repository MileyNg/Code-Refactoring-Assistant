#include <stdio.h>

int main(void) {
  int n, i, a[100];

  scanf("%d", &n);

  for (i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }

  for (; n--; ) {
    printf("%d", a[n]);
    if (n > 0) {
      putchar(' ');
    }
  }

  putchar('\n');

  return 0;
}