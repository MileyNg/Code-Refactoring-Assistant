#include <stdio.h>

int isprime(int);

main(){

  int kosu,n[10000],ans = 0;
  int i,j;

  scanf("%d",&kosu);

  for(i = 0 ; i < kosu ; i++){
    scanf("%d",&n[i]);
    if(isprime(n[i]) == 1) ans++;
  }

   printf("%d\n",ans);

  return 0;

}



int isprime(int x){

  int i;

  if(x <= 1) return 0;

  for(i = 2 ; i <= x - 1; i++){
    if(x % i == 0) return 0;
  }

  return 1;

}