#include <stdio.h>

int main(void)
{
	int n, i, j;
	int num[5000];
	int sum, big;
	
	while (1){
		scanf("%d", &n);
		
		if (n == 0){
			break;
		}
		
		for (i = 0; i < n; i++){
			scanf("%d", &num[i]);
		}
		
		big = num[0];
		
		for (i = 0; i < n; i++){
			sum = 0;
			for (j = i; j < n; j++){
				sum += num[j];
				if (sum > big){
					big = sum;
				}
			}
		}
		printf("%d\n", big);
	}
	
	
	return (0);
}