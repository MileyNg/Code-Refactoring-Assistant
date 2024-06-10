#include <stdio.h>

int main(void){
	int n, i;
	double x1, y1, x2, y2, x3, y3, x4, y4;
	double dx1, dy1, dx2, dy2;
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		scanf("%lf %lf %lf %lf %lf %lf %lf %lf", &x1, &y1, &x2, &y2, &x3, &y3, &x4, &y4);
		dx1 = (x2 - x1); dy1 = (y2 - y1);
		dx2 = (x4 - x3); dy2 = (x4 - x3);
		if((dx1 * dy2) == (dx2 * dy1))	printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}