#include <stdio.h>

int main(void) {
	double a, b, c, d, e, f, x, y;

	while(scanf("%lf %lf %lf %lf %lf %lf", &a, &b, &c, &d, &e, &f) != EOF){
		x = (c*e - b*f) / (a*e - b*d);                          
        y = (a*f - d*c) / (a*e - b*d);
		if(x < 0) x = (double)((int)(x * 1000 - 0.5) / 1000);
		else x = (double)((int)(x * 1000 + 0.5) / 1000);
		if(y < 0) y = (double)((int)(y * 1000 - 0.5) / 1000);
		else y = (double)((int)(y * 1000 + 0.5) / 1000);
		printf("%.3lf %.3lf\n", x, y);
	}
	return 0;
}