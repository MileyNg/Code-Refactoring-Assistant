#include <stdio.h>

int main(void)
{
	char str[20];
	int a, b, c;
	
	scanf("%s", str);
	a = 0;
	
	while (str[a] != '\0') {
		a++;
	}
	
	a -= 1;
	for (b = a; b >= 0; b--) {
		printf("%c", str[b]);
	}
	printf("\n");
	
	return (0);
}	