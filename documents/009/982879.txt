#include<stdio.h>
main(){
  long a=100000;
  int b=0;
  int  c=0;
  int  d=0;
  long e=0;
  long f=0;
  scanf("%d",&b);
  for(c=0;c<b;c++){
    e=a/20;
    a=a+e;
    if(a%1000!=0){
      a=a/1000*1000+1000;
    }
  }
  printf("%d\n",a);
  return 0;
}