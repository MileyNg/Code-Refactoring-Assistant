#include<stdio.h>
#include<stdlib.h>

void push(int);
int pop(void);
int stack[100];
int stacksum=0;

int main(void)
{
  int i,x,y,data1;
  char data[100];
  
  for(i=0;scanf("%s",data)!= EOF;i++){
    
    if(data[0]=='+') {
      x = pop();
      y = pop();
      push(x+y);
    }
    else if(data[0]=='-'){ 
      x = pop();
      y = pop();
      push(y-x);
    }
    else if (data[0] == '*'){
      x = pop();
      y = pop();
      push(x*y);
    }
    else{
      data1 = atoi(data);
      push(data1);
    }
  }
  
  printf("%d\n",stack[0]);
  return 0;
}
void push(int data){
  stack[stacksum]=data;
  stacksum++;
}

int pop(void){
  
  stacksum--;
  return stack[stacksum];
} 