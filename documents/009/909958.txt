#include<stdio.h>

int main(){
  int a=0,b=0;

  scanf("%d%d",&a,&b);

  if(a < 1 || a > 1000000000 || b < 1 || b > 1000000000){
    return 0;
  } 

  while(a != b){
    if(a > b){
      a = a-b;
    }
    else b =b-a;
  }
  printf("%d\n",a);

  return 0;
}