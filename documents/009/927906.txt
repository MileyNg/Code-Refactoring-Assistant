#include<stdio.h>
int main(void){
	int i, j, n, a;
	double x[4], y[4];
	scanf("%d", &n);
	for (i = 0; i < n; i++){
		for (j = 0; j < 4; j++){
			scanf("%lf%lf", &x[j], &y[j]);
		}
		a = (y[0] - y[1]) / (x[0] - x[1])
			- (y[2] - y[3]) / (x[2] - x[3]);
		if (-0.000001<=a && a<=0.000001){
			printf("YES\n");
		}
		else{
			printf("NO\n");
		}
	}
	return 0;
}