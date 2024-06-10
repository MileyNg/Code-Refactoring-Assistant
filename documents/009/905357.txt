#include <stdio.h>

int main(void) {
	int a, b, c, d, e, f;
	float x, y;
	while(scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f) != EOF){

		y = (float)(c*d - a*f) / (b*d - a*e);
		x = (float)(c*e - b*f) / (a*e - b*d);
		printf("%.3f %.3f\n", x, y);
	}
	return 0;
}