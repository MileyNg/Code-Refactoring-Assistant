#include <stdio.h>
int main(void) {
	int a, b, sum, count;
	while(scanf("%d %d", &a, &b) != EOF){
		sum = a + b;
		count = 0;
		while(sum > 0){
			sum = sum / 10;
			count++;
		}
		printf("%d\n", count);
	}
	return 0;
}