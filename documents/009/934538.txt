#include<stdio.h>
#include<stdlib.h>
#include<string.h>
 
int main(){
  int num[100];
  int i=0;
  char s[100];
 
  while( scanf("%s", s) != EOF ){
    if ( s[0] == '+' ){
      num[i-2] += num[i-1];
      i = i-1;
    } else if ( s[0] == '-' ){
      num[i-2] -= num[i-1];
      i = i-1;
    } else if ( s[0] == '*' ){
      num[i-2] *= num[i-1];
      i = i-1;
    } else {
      num[i] = atoi(s);
      i = i+1;
    }
  }
 
  printf("%d\n",num[0]);
 
return 0;
}