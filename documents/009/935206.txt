#include<stdio.h>
int main(void)
{
  int a,b,c;

  while(scanf("%d %d",&a,&b)!=EOF){
    int count=0;
    c=a+b;
    while(c>0){
      c/=10;
      count+=1;
    }
    printf("%d\n",count);
  }

  return 0;
}