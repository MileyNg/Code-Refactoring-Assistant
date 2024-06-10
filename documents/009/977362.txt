#include <stdio.h>

double func(double a ,double b,double c,double d,double e,double f){
	//return (c*d-a*f)/(b*d-a*e);
	return (c*e-b*f)/(a*e-b*d);
}

int main(void){
	double a,b,c,d,e,f,x,y;
	while(scanf("%lf %lf %lf %lf %lf %lf",&a,&b,&c,&d,&e,&f) != EOF){
		//y=func(a,b,c,d,e,f);
		//x=(c-b*y)/a;
		//func(a,b,c,d,e,f,x,y);
		x=func(a,b,c,d,e,f);
		y=((c-(a*x))/b);
		printf("%.3lf %.3lf\n",x,y);
	}
	return 0;
}