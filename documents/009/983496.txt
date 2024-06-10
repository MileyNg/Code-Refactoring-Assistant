#include <stdio.h>
#include <stdlib.h>

int main(void){
	int n, i, j, k, max, sum;
	int *a;
	while(scanf("%d", &n) != EOF){
		if(n == 0)	break;
		max = 0;
		sum = 0;
		a = malloc(sizeof(int)*n);
		for(i = 0; i < n; i++){
			scanf("%d", a+i);
		}

		for(i = 0; i < n-1; i++){
			for(j = i+1; j < n; j++){
				for(k = i; k <= j; k++){
					sum += a[k];
				}
				
				if(sum > max){
					max = sum;
				}
				sum = 0;
			}
		}

		printf("%d\n", max);
	}
	return 0;
}