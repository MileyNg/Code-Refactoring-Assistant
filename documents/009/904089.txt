#include <stdio.h>
#include <string.h>

int main(void)
{
	int l;
	char str[20];
	char t;
	int i, j;

	scanf("%s", str);

	l = strlen(str);
	for(i = 1; i < l; i++){
		for(j = 0; j < l - i; j++){
			t = str[j];
			str[j] = str[j+1];
			str[j+1] = t;
		}
	}

	printf("%s\n", str);

	return 0;
}