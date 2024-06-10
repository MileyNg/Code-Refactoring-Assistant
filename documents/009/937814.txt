#include <stdio.h>

int main(void)
{
	int i;
	char str[20];
	
	scanf("%s", str);
	
	i = 0;
	while (str[i] != '\0'){
		i++;
	}
	i--;
	while (i >= 0){
		printf("%c", str[i]);
		i--;
	}
	printf("\n");
	
	return (0);
}