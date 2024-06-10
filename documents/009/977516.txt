#include<stdio.h>
int main(){

  int n,i, m=100000;

  scanf("%d",&n);

  for(i=0;i<n;i++){
    m=m*1.05;
    m=(m+999)/1000;
    m*=1000;
  }
  printf("%d\n",m);

  return 0;
}