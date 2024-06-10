#include<stdio.h>//連立方程式
#include<math.h>

int main(void)
{
	double a,b,c,d,e,f,x,y;
	
	while(scanf("%lf %lf %lf %lf %lf %lf", &a, &b, &c, &d, &e, &f) != EOF){
		x = (c - (f / e) * b) / (a - (d / e) * b);
		y = (c - x * a) / b;
		if (x == -0) x = 0;
		if (y == -0) y = 0; 
		printf("%4.3f %4.3f\n",x,y);
	}
	return 0;
}