#pragma warning (disable:4996)
#include <stdio.h>
#include <string.h>

int inputStr(char *str){
	scanf(" %s", str);
	if (!strcmp(str, "-")) return 0;
}
void sortStr(char *str){
	int num, h;
	char tmp[256];
	scanf("%d", &num);
	while (num--){
		scanf("%d", &h);
		strcpy(tmp, str);
		strcpy(str, tmp + h);
		strncat(str, tmp, h);
	}
}
int main(void){
	char str[256];
	while (inputStr(str)){
		sortStr(str);
		printf("%s\n", str);
	}
	return 0;
}