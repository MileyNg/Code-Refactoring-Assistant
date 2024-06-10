#include <stdio.h>

int main(void)
{
	int n;
	int Prime_n;
	int i, j;
	int P;
	
	while (scanf("%d", &n) != EOF){
		Prime_n = 0;
		
		for (i = 1; i != n + 1; i++){
			P = 0;
			for (j = 1; j != n + 1; j++){
				if (i % j == 0 && i != 1){
					P++;
				}
			}
			if (P == 2){
				Prime_n++;
			}
		}
		printf("%d\n", Prime_n);
	}
	return (0);
}