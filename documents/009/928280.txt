#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
  int x,a[101],b=1;
  char s[100];

  while( scanf("%s", s) != EOF ){
    if ( s[0] == '+' ){
      a[b-2] = a[b-2] + a[b-1];  
      b--;
    } else if ( s[0] == '-' ){
      a[b-2] = a[b-2] - a[b-1];
      b--;
    } else if ( s[0] == '*' ){
      a[b-2] = a[b-2] * a[b-1]; 
      b--;
    } else {
      x = atoi(s);
      a[b] = x;
      b++;
    }
  }
  printf("%d\n",a[b-1]);
  return 0;
}