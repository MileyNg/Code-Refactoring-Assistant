

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
  int y[100],i=0,x=0;
  char s[100];

  while( scanf("%s", s) != EOF ){
    if ( s[0] == '+' ){
      y[i-2] = y[i-2] + y[i-1];
      i--;
     }
 
    else if ( s[0] == '-' ){
      y[i-2] = y[i-2] - y[i-1];
      i--;
    }
 
    else if ( s[0] == '*' ){
      y[i-2] = y[i-2] * y[i-1];
      i--;
    }
 
    else {
      x = atoi(s);
      y[i] = x;
      i++;
    }  
  } 
  printf("%d\n",y[i-1]);
  return 0;
}