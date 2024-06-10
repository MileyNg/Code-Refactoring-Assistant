#include<stdio.h>
#include<math.h>
#include<string.h>
int main(void)
{
  double a,b,c,d,e,f;
  while(scanf("%lf %lf %lf %lf %lf %lf",&a,&b,&c,&d,&e,&f)!=EOF){
    double x,y;
	x=(c*e-b*f)/(a*e-b*d);
	y=(a*f-c*d)/(a*e-b*d);
	if(x==0)
	  x=0;
	if(y==0)
	  y=0;
	printf("%.3f %.3f\n",x,y);
  }

  return 0;
}