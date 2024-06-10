#include <stdio.h>

int main(void) {
	int a, b, c, d, e, f;
	float x, y;
	while(scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f) != EOF){

		y = (float)(c*d - a*f) / (b*d - a*e);
		x = (float)(c*e - b*f) / (a*e - b*d);
		if(x < 0) x = (float)((int)(x * 1000 - 0.5) / 1000);
		else 	x = (float)((int)(x * 1000 + 0.5) / 1000);
		if(y < 0) y = (float)((int)(y * 1000 - 0.5) / 1000);
		else y = (float)((int)(y * 1000 + 0.5) / 1000);
		printf("%.3f %.3f\n", x, y);
	}
	return 0;
}