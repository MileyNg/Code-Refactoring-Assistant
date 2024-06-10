#include <stdio.h>
#include <math.h>

int isPrime(int);

main(){
  int N,i,a,j,count=0;

  scanf("%d", &N);

  for(i=0; i<N; i++){
    scanf("%d",&a);
    if((isPrime(a)) == 0){
      count++;
    }
  } 
  printf("%d\n", count);
  return 0;
}

int isPrime(int b){
  int i;

  for(i=2; i<=sqrt(b); i++){
    if(b % i == 0){
      return 1;
    }
  }
  return 0;
}