#include<stdio.h>
#define MIN(a,b) (((a)<(b)) ? (a) : (b))
#define MAX(a,b) (((a)>(b)) ? (a) : (b))

int GCD(int a,int b)
{
  if(a==0||b==0) return MAX(a,b);
  else return GCD(MAX(a,b)%MIN(a,b),MIN(a,b));
}

int LCM(int a,int b)
{
  int c;
  c=GCD(a,b);
  return (a/c)*(b/c)*c;
}

int main(){
  int a,b;
  while(scanf("%d %d",&a,&b)!=EOF)
    {
      printf("%d %d\n",GCD(a,b),LCM(a,b));
    }
  return 0;
}