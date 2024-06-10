#include<stdio.h>
#define MIN(a,b) (((a)<(b)) ? (a) : (b))
#define MAX(a,b) (((a)>(b)) ? (a) : (b))
#define RATE 5
int main(){
  int i,n,sum=100000;
  scanf("%d",&n);
  for(i=0;i<n;i++)
    {
      sum = sum*(100+RATE)/100;
      sum = ((sum%1000)>0)?(sum/1000+1)*1000:(sum/1000)*1000;
    }
  printf("%d\n",sum);
  return 0;
}