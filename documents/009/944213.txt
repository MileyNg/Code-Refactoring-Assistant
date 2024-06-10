#include <stdio.h>

int pn[1000000];

int main(void)
{
	int n;
	int i, j;
	int total;
	
	for (i = 2; i < 1000000; i++){
		//printf("%d\n", i);
		if (pn[i] == 0){
			for (j = i + i; j < 1000000; j += i){
				//if (j % i == 0){
					pn[j] = 1;
				//}
			}
		}
	}
	while (scanf("%d", &n) != EOF){
		total = 0;
		for (i = 2; i <= n; i++){
			if(pn[i] == 0){
				total++;
			}
		}
		printf("%d\n", total);
	}
	
	return (0);
}