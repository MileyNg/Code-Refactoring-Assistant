#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
  int i;
  char s[100];
  int x[100];
  for(i = 0;i < 100;i++){
  x[i] =0;
  }
  i=0;
  while( scanf(" %s", s) != EOF ){
    if ( s[0] == '+' ){
      x[i-2]=x[i-1]+x[i-2];
      i--;
    } else if ( s[0] == '-' ){
      x[i-2]=x[i-2]-x[i-1];
      i--;
    } else if ( s[0] == '*' ){
      x[i-2]=x[i-1]*x[i-2];
      i--;
    } else {
      x[i] = atoi(s);
      i++;
    }
  }

  printf("%d\n",x[i-1]);
    
    return 0;
  }