#include <stdio.h>

int main(){
	int n, i, a, min, max;
	long sum;
	scanf("%d %d", &n, &min);
	max = min;
	sum = min;
	for(i = 1; i < n; i++){
		scanf("%d", &a);
		if(min > a){
			min = a;
		}
		if(max < a){
			max = a;
		}
		sum += a;
	}
	printf("%d %d %d\n", min, max, sum);
	return 0;
}