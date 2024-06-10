#include<stdio.h>

main(){
  int week;
  int i;
  int res = 100000;
  int l;

  scanf("%d", &week);

  for(i = 0 ; i < week ; i++){
    res += res * 0.05;
  }

  l = res % 10000;
  res -= l;
  l /= 1000;
  if(l >= 5) res += 10000;

  printf("%d\n", res);

  return 0;
}