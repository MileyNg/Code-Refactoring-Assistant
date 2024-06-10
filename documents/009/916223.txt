#include<stdio.h>
int main(){
  int a, b, c;

  while(scanf("%d %d %d", &a, &b, &c) != EOF){
    if(a > b && a > c){
      if(a * a == b * b + c * c){
        printf("YES\n");
      }
    }else if(b > a && b > c){
      if(b * b == a * a + c * c){
        printf("YES\n");
      }
    }else if(c < a && c < b){
      if(c * c == a * a + c * c){
        printf("YES\n");
      }
    }else{
      printf("NO\n");
    }
  }
  return 0;
}