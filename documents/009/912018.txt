#include <stdio.h>
#include <string.h>

int main(void) {
	int i;
	char s[21];
	scanf("%s",&s);
	for (i=strlen(s)-1;i>-1;i--){
		printf("%c",s[i]);
	}
	printf("\n");
	return 0;
}