#include <stdio.h>
#include <math.h>
#define N 10000
int sosuu(int);
int main(){
  int n,i,count=0;
  int A[N+1];
  scanf("%d",&n);
  for(i=1;i<=n;i++) scanf("%d", &A[i]);
  for(i=1;i<=n;i++){
    if(sosuu(A[i])==0) count++;
  }
  printf("%d\n",count);
  return 0;
}

int sosuu(int x){
  int i;
  for(i=2;i<=sqrt(x);i++){
    if((x%i)==0) return 1;
  }
  if(x!=1) return 0;
}