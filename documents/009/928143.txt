#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
  int i = 0;
  int x[100];
  char s[100];
  
  while( scanf("%s", s) != EOF){
    if ( s[0] == '+' ){
      i--;
      x[i] += x[i+1];
    } 
    else if ( s[0] == '-' ){
      i--;
      x[i] -= x[i+1];
    } 
    else if ( s[0] == '*' ){
      i--;
      x[i] *= x[i+1];
    } 
    else {
      i++;
      x[i] = atoi(s);
    }
  }
  printf("%d\n",x[i]);
  return 0;
}