#include <stdio.h>

int main(void){
	char str[50];
	int i = 0;
	fgets(str, sizeof(str), stdin);
	while(str[i] != '\n'){
		i++;
	}
	for(i = i - 1; i >= 0; i--){
		printf("%c", str[i]);
	}
	printf("\n");
	
	return 0;
}