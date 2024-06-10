#include <stdio.h>

int main(void) {
	int cars[10] = {0};	
	int order,i=0;
	
	while( scanf("%d", &order) != EOF ) {
		if(order == 0) {
			printf("%d\n", cars[i-1]);
			cars[i--] = 0;
		}
		else if(1<=order && order<=10) {
			cars[i++] = order;
		}
		else continue;
	}
	
	return 0;
} 