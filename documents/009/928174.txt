#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
  int x,i=0,num[100],ans;
  char s[100];

  while( scanf("%s", s) != EOF ){
    if ( s[0] == '+' ){
      ans = num[i-2] + num[i-1];
      i -= 2;
      num[i] = ans;
      i++;
    }
    else if ( s[0] == '-' ){
      ans = num[i-2] - num[i-1];
      i -= 2;
      num[i] = ans;
      i++;

    }
    else if ( s[0] == '*' ){
      ans = num[i-2] * num[i-1];
      num[i] = ans;
      i++;

      
    }
    else {
      x = atoi(s);
      num[i] = x;
      i++;
      
    }
  }
  
  printf("%d\n",num[i-1]);
  return 0;
}