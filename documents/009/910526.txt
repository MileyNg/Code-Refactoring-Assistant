#include <stdio.h>
#include <math.h>
#define N 10000


void prime(int);

int main()
{
  int n,i;
  int array[N];
  int count=0,f,k=0,j;
  
  
  scanf("%d", &n);
  
  for ( i = 0; i < n; i++ ){
    scanf("%d", &array[i]);
  }
  for(j=0;j<n;j++){
    k=0;
    for(i=2;i<=sqrt(array[j]);i++){
      f=array[j]%i;
      if(f==0){
	k=1;
      }
    }
    if(k==0){
	count++;
    }
  }
  printf("%d\n",count);
}