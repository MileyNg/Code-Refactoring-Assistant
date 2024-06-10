#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
  int x;
  char s[100];
  int A[100];
  int i=0;
  int count=0;
  
  while( scanf("%s", s) != EOF ){
    if ( s[0] == '+' ){
      A[i-1]=A[i]+A[i-1];
      i--;
    } else if ( s[0] == '-' ){
      A[i-1]=A[i-1]-A[i];
      i--;
    } else if ( s[0] == '*' ){
      A[i-1]=A[i-1]*A[i];
      i--;
    } else {
      i++;
      x = atoi(s);
      A[i]=x;  
    }
  }
  printf("%d\n",A[1]);

  return 0;
}