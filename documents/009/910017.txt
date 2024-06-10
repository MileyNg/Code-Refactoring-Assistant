#include<stdio.h>
#include<math.h>

int gdb(int,int);
void swap(int, int);

int main(){
  int a,b;
  
  scanf("%d %d",&a,&b);
  printf("%d\n",gdb(a,b) );
}

int gdb(a,b){
  int r,d;
  if(a<b)
    swap(a,b);
  while(b>0){
    r=a%b;
    a=b; 
    b=r;}
  return a;
}

void  swap(int x, int y)
{
  int  work;
  work = x;
  x = y;
  y = work;
}