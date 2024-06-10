#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(void)
{
  int a,b,c,d,e,f;
  double x,y,det;
  while(scanf("%d%d%d%d%d%d",&a,&b,&c,&d,&e,&f)!=EOF){
    det=(double)(a*e-b*d);
    x=(double)(c*e-b*f)/det;
    y=(double)(-d*c+a*f)/det;
    printf("%.3lf %.3lf\n",x,y);
  }

  return 0;
}