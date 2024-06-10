#include<stdio.h>
main(){
  int s=0;
  int H=0;
  int M=0;
  scanf("%d",&s);
  while(s>3599){
    s=s-3600;
    H++;
  }
  while(s>59){
    s=s-60;
    M++;
  }
  printf("%d:%d:%d\n",H,M,s);
  return 0;
}