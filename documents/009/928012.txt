#include<stdio.h>
#include<stdlib.h>
#define max 10000
static int stack[max+1],p;
push(int v){
  stack[p++]=v;
}
int pop1(){
  return stack[--p];
}
int pop2(){
  return stack[p-=2];
}
int pop3(){
  return stack[++p];
}
stackinit() {
  p=0;
}
int stackempty(){
  return !p;
}
main()
{
  char c[100];
  int x;
  stackinit();
  while(scanf("%s",c)!=EOF)
    {
      x=0;
      if(c[0]=='+')x=pop1()+pop1();
      else if(c[0]=='*')x=pop1()*pop1();
      else if(c[0]=='-')x=pop2()-pop3();      else x=atoi(c);
      push(x);
    }
  printf("%d\n",x);
  return 0;
}