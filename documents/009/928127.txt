#include<stdio.h>
#include<stdlib.h>
#include<string.h>

static int stack[1000],p;

int pop(){
  return stack[--p];
}
push(int v){
  return stack[p++]=v;
}
int main(){
  int x;
  char s[100];
  
  while( scanf("%s", s) != EOF ){
    if ( s[0] == '+' ){
      x=pop()+pop();     
    } 
    else if ( s[0] == '-' ){
      x=pop()-pop();
    }
    else if ( s[0] == '*' ){
      x=pop()*pop();
    }
    else {
      x = atoi(s);
    }
    push(x);
  }
  printf("%d\n",x);
  
  return 0;
}