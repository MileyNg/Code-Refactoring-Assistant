#include <stdio.h>

int main(void)
{
	float a, b, c, d, e, f;
	float aa, bb, cc, dd, ee, ff;
	float x, y;
	
	while (scanf("%f %f %f %f %f %f", &a, &b, &c, &d, &e, &f) != EOF){
		aa = a * d; bb = b * d; cc = c * d;
		dd = d * a; ee = e * a; ff = f * a;
		bb -= ee; cc -= ff;
		cc /= bb; y = cc;
		c -= b * y;
		c /= a;
		x = c;
		
		printf("%.3f %.3f\n", x, y);
	}
	
	return (0);
}