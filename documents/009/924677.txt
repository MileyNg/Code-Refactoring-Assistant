#include <stdio.h>

int main(void)
{
	int a, b, c, d, e;
	int z, zz, x, xx;
	
	while (scanf("%d", &a)!=EOF){
		z = 0;
		for (b = 0; b <= 9; b++) {
			for (c = 0; c <= 9; c++) {
				for (d = 0; d <= 9; d++) {
					for (e = 0; e <= 9; e++) {
						if ((b + c + d + e) == a) {
							z++;
						}
					}
				}
			}
		}
		printf("%d\n", z);
	}
	
	return (0);
}	