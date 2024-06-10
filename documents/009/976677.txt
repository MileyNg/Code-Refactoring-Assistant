#include<stdio.h>

int main(void)
{
  int num = 100000, n,i;

  scanf("%d", &n);

  for(i=1; i<=n; i++){
    num = num * 1.05;
  }

  num = num / 10000;
  num = num + 1;
  num = num * 10000;

  printf("%d\n", num);

  return 0;
}