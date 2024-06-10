#include<stdio.h>
main(){
  int n,i;
  double a=100000;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    a=a*1.05;
    a=a/1000+0.9;
    a=(int)a*1000;
  }
  printf("%g\n",a);
  return 0;
}