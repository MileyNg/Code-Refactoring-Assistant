#include <stdio.h>

int main(void)
{
	char d, e, f;
	char str[4];
	int a, b;
	
	str[0] = '1';
	str[1] = '0';
	str[2] = '0';
	while (scanf("%c,%c", &d, &e) != EOF){
		if (d == 'A') {
			if (e == 'B') {
				f = str[0];
				str[0] = str[1];
				str[1] = f;
			}
			else if (e == 'C') {
				f = str[0];
				str[0] = str[2];
				str[2] = f;
			}
		}
		else if (d == 'B') {
			if (e == 'A') {
				f = str[1];
				str[1] = str[0];
				str[0] = f;
			}
			else if (e == 'C') {
				f = str[1];
				str[1] = str[2];
				str[2] = f;
			}
		}
		else if (d == 'C') {
			if (e == 'A') {
				f = str[2];
				str[2] = str[0];
				str[0] = f;
			}
			else if (e == 'B') {
				f = str[2];
				str[2] = str[1];
				str[1] = f;
			}
		}
	}
	for (a = 0; a < 3; a++) {
		if (str[a] == '1') {
			b = a;
		}
	}
	if (b == 0) {
		printf("A\n");
	}
	else if (b == 1) {
		printf("B\n");
	}
	else if (b == 2) {
		printf("C\n");
	}
	
	return (0);
}	