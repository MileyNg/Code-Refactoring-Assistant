#include<stdio.h>

main(){
  int a, b, rest;
  scanf("%d%d", &a, &b);

  printf("%d\n", gcd(a, b));
  return 0;
}

int gcd(int x, int y){
  int rest;
  rest = x % y;
  while(rest != 0) {
    x = y;
    y = rest;
    rest = x % y;
  }
  return y;
}