#include<stdio.h>
main(){
  int a;
  int b;
  int c;
  scanf("%d %d %d",&a,&b,&c);
  if(a < b && b < c){
    printf("%d %d %d\n",a,b,c);
  }
  if(a < c && b > c){
    printf("%d %d %d\n",a,c,b);
  }
  if(a > b && c < b){
    printf("%d %d %d\n",c,b,a);
  }
  if(c < a && a < b){
    printf("%d %d %d\n",c,a,b);
  }
  if(b < a && a < c){
    printf("%d %d %d\n",b,a,c);
  }
  if(b < c && c < a){
    printf("%d,%d,%d\n",b,c,a);
  }  
  return 0;
}