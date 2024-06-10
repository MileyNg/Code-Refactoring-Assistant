#include <stdio.h>

int num[1000000];

int main(void)
{
	int n, i, j;
	int count;
	
	for (i = 0; i <= 999999; i++){
		num[i] = 1;
	}
		
	num[0] = 0;
	num[1] = 0;
	
	for (i = 2; i * i <= 999999; i++){
		if (num[i] == 1){
			for (j = i * i; j <= 999999; j += i){
				num[j] = 0;
			}
		}
	}
	
	while (scanf("%d", &n) != EOF){
		count = 0;
		for (i = 0; i <= n; i++){
			if (num[i] == 1){
				count++;
			}
		}
		printf("%d\n", count);
	}
	return (0);
}