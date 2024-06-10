#include <stdio.h>

int main(void) {
	char str[21];
	int i, n;
	scanf("%20s", &str);
	n = strlen(str);
	for(i = n; i > 0; i--) printf("%c", str[i-1]);
	printf("\n");
	return 0;
}