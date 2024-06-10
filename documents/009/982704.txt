#include<stdio.h>
main(){
  int a=0;
  int b=0;
  int c=0;
  int d=0;
  int e=0;
  scanf("%d %d %d",&a,&b,&c);
  for(d=a;d<b+1;d++){
    if(c%d==0){
      e=e+1;
    }
  }
  printf("%d\n",e);
  return 0;
}