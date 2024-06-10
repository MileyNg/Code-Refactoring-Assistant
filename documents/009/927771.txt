#include <stdio.h>

int main(void) {
	int a, b;
	char c;
	while(scanf("%d %c %d", &a, &c, &b) == 3) {
		switch(c) {
			case '+':
				printf("%d\n", a+b);
				break;
			case '-':
				printf("%d\n", a-b);
				break;
			case '/':
				printf("%d\n", a/b);
				break;
			case '*':
				printf("%d\n", a*b);
				break;
			case '?':
				return 0;
		}	
	}
	
	return 0;
}