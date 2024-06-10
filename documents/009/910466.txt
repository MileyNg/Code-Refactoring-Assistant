#include <stdio.h>
#include <math.h>

#define N 12

int isPrime(int);

int main(void){
  int i,j,num[N],count=0,temp[N];

  for(i=0; i<N; i++){
    scanf("%d",&num[i]);
  }

  printf("\n");

  for(i=0; i<N; i++){
    if( isPrime(num[i]) ){
      //printf("%d \n",num[i]);
      count++;
      //printf("count=%d\n",count);
      for(j=0; j<i; j++){
	if(num[i]==num[j]){
	  count--;
	  //printf("count=%d\n",count);
	}
      }
    }
  }
  printf("%d\n",count);
  
  return 0;
}

int isPrime(int x){
  int i;
  //int sqx;
  //sqx = (int)sqrt((double)x);
  if(x == 2) return 1;
  if((x < 2) || (x % 2 == 0))return 0;
  for(i=3; i<=x/2; i+=2){
    if(x%i == 0){
      return 0;
    }
  }
  return 1;
}