#include <stdio.h>

int main(void) {
	int a, b, c, d, e, f;
	double x, y;
	while(scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f) != EOF){

		y = (double)(c*d - a*f) / (b*d - a*e);
		x = (double)(c*e - b*f) / (a*e - b*d);
		if(x < 0) x = (double)((int)(x * 1000 - 0.5) / 1000);
		else 	x = (double)((int)(x * 1000 + 0.5) / 1000);
		if(y < 0) y = (double)((int)(y * 1000 - 0.5) / 1000);
		else y = (double)((int)(y * 1000 + 0.5) / 1000);
		printf("%.3lf %.3lf\n", x, y);
	}
	return 0;
}