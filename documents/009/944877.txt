#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
  int x, pt = 0;
  int stack[100];
  char s[100];

  while(scanf("%s", s) != EOF){
    if(s[0] == '+'){
      stack[pt - 2] = stack[pt - 2] + stack[pt - 1];
      pt--;
    }else if(s[0] == '-'){
      stack[pt - 2] = stack[pt - 2] - stack[pt - 1];
      pt--;
    }else if(s[0] == '*'){
      stack[pt - 2] = stack[pt - 2] * stack[pt - 1];
      pt--;
    }else{
      x = atoi(s);
      stack[pt] = x;
      pt++;
    }
  }

  printf("%d\n", stack[pt - 1]);

  return 0;
}