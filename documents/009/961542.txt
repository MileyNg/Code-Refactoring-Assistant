#include <stdio.h>

int main(void) {
	char str[20];
	
	scanf("%s", str);
	
	int i,end;
	for(i=0;i<=20;i++){
		if(str[i] == '\0'){
			end = i;
			break;
		}
	}
	
	for(i=end-1; i>=0; i--)
		printf("%c", str[i]);
	printf("\n");
	
	return 0;
	
}