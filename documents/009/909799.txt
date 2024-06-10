#include<stdio.h>

int main(){
  int a,b,i,a1;
  scanf("%d %d",&a,&b);
  
  while(1){
    a1 = a;
    a = b%a;
    b = a1;
    if(a==0){
      printf("%d\n",b);
      break;
    }
  }
  return 0;
}