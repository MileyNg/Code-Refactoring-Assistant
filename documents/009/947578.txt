#include <stdio.h>

int main(void) {
	int stack[1000];
	int car, p = 0;
	
	while(scanf("%d\n", &car) == 1) {
		if(car == 0) {
			if(p > 0) {
				printf("%d\n", stack[p-1]);
				p--;
			}
		} else {
			stack[p] = car;
			p++;
		}
	}
	return 0;
}