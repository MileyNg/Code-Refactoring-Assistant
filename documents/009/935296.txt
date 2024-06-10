// AOJ0021
#include<stdio.h>
#include<math.h>

int main(){
	double x1, y1, x2, y2, x3, y3, x4, y4;
	int n, i;
	double d1, d2;
	scanf("%d", &n);
	
	for(i = 0; i < n; i++){
		scanf("%lf %lf %lf %lf %lf %lf %lf %lf", &x1, &y1, &x2, &y2, &x3, &y3, &x4, &y4);
		d1 = (y2-y1)/(x2-x1);
		d2 = (y4-y3)/(x4-x3);
		if(d1 == d2)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}