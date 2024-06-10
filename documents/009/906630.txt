#include <stdio.h>

int main(void) {
	int a, b, sum, d;
	
	while (scanf("%d %d", &a, &b) > 0) {
		sum = a + b;
		
		d = 0;
		do {
			sum /= 10;
			d++;
		} while (sum > 0);
		
		printf("%d\n", d);
	}
	
	return 0;
}