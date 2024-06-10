#include<stdio.h>
int main(void)
{
  int n,i;
  int money=100000;

  scanf("%d",&n);

  for(i=0;i<n;i++){
    money*=1.05;
    if(money%1000!=0)
      money+=1000-money%1000;
  }

  printf("%d\n",money);

  return 0;
}