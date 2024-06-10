#include<stdio.h>
#include<stdlib.h>
#include<string.h>

static int stack[101],p;

void push(int);
int pop();

void push(int x){
  stack[p++]=x;
}

int pop(){
  return stack[--p];
}


int main(){
  int x,p=0,a=0,b=0;
  char s[100];
  
  while(scanf("%s",s) != EOF){
    
    if(s[0] == '+'){
      push(pop()+pop());
    } 

    else if(s[0] == '-'){
      a=pop();
      b=pop();
      push(b-a);
    } 

    else if(s[0] == '*'){
      push(pop()*pop());
    }

    else {
      x = atoi(s);
      push(x);
    }
  }

  printf("%d\n",stack[p]);  
  
  return 0;
}