#include <stdio.h>

char prime[1000000];

int main(void)
{
	int n;
	
	while (scanf("%d", &n) != EOF){
		int count = 0;
		int i, j;
		
		if (n > 1){
			count++;
		}
		for (i = 3; i <= n; i += 2){
			if (prime[i] == ~0){
				continue;
			}
			else if (prime[i] != 0){
				count++;
				continue;
			}
			else if (i % 2 == 0){
				continue;
			}
			for (j = 3; j <= i / 2; j += 2){
				if (i % j == 0){
					prime[i] = ~0;
					break;
				}
			}
			if (i / 2 < j){
				prime[i] = 1;
				count++;
			}
		}
		printf("%d\n", count);
	}
	
	return 0;
}