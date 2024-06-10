#include<stdio.h>
#include<ctype.h>
#include<string.h>
main(){
  int a=0;
  int b=0;
  int c=0;
  int d=0;
  char A;
  while(scanf("%c",&A)!=EOF){
    if('A'<=A&&A<='Z'){
      A=tolower(A);
    }
    else if('a'<=A&&A<='z'){
      A=toupper(A);
    }
    printf("%c",A);
  }
  return 0;
}