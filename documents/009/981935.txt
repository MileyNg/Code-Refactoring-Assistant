#include<stdio.h>
#include<stdlib.h>

int main(){
  
  int a;
  int b;
  int c,
    d;
  
  while(scanf("%d %d",&a,&b)!=EOF){
  
    // while(a[i]!=0){
    c=a+b;
    d=0;
    while(c!=0){
      c/=10;
      d++;
    }
    printf("%d\n",d);
  }
   
  return 0;
}