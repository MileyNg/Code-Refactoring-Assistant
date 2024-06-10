#include <stdio.h>

int main() {
	float a, b, c, d, e, f;
	double x,y,z;
	while (scanf("%f %f %f %f %f %f", &a, &b, &c, &d, &e, &f) != EOF)
	{
		x = b*f - c*e;
		y = c*d - a*f;
		z = b*d - a*e;
		printf("%.3lf %.3lf\n", x/z, y/z);
	}
	return 0;
}