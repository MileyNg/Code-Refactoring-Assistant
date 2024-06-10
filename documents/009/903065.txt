#include<stdio.h>

main(){
  int week;
  int i;
  int res = 100000;
  int l;

  scanf("%d", &week);

  for(i = 0 ; i < week ; i++){
    res += res * 0.05;
    res += 999;
    l = res % 1000;
    res -= l;
  }

  printf("%d\n", res);

  return 0;
}