#include <stdio.h>

int main(void)
{
	int array[5000];
	int n;
	
	scanf("%d", &n);
	while (n != 0){
		int i;
		int max;
		for (i = 0; i < n; i++){
			scanf("%d", &array[i]);
		}
		max = -(100000 * 5000);
		for (i = 0; i < n; i++){
			int j;
			int sum = 0;
			for (j = i; j < n; j++){
				sum += array[j];
				if (max < sum){
					max = sum;
				}
			}
		}
		printf("%d\n", max);
		
		scanf("%d", &n);
	}
	
	return 0;
}