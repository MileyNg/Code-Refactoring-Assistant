#include <stdio.h>

int main(void)
{
  int a, b, c;
  int zero;
  int cnt = 0;
  int i;

  scanf("%d %d %d", &a, &b, &c);

  for(i = a;i <= b;i++){
    zero = c % i;
    if(zero == 0){
      cnt++;
    }
  }

  printf("%d\n", cnt);

  return 0;
}