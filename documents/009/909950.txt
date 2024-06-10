#include<stdio.h>

int main(void)
{
  int a,b,c=100;
  scanf("%d%d",&a,&b);
  if(a<b)
    {
      c = a;
      a = b;
      b = a;
    }
  while(c != 0)
    {
      c = a%b;
      a = b;
      b = c;
    }
  printf("%d\n",a);
  return 0;
}