#include<stdio.h>//連立方程式
//#include<math.h>

int main(void)
{
	float a,b,c,d,e,f,x,y;
	
	while(scanf("%f %f %f %f %f %f", &a, &b, &c, &d, &e, &f) != EOF){
		x = (c - (f / e) * b) / (a - (d / e) * b);
		y = (c - x * a) / b;
		printf("%.3f %.3f\n",x,y);
	}
	return 0;
}