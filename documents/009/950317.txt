#include <stdio.h>

int main(void) {
	int n = 0, num[10] = {0};
	while(scanf("%d", &num[n]) != EOF){
		if(num[n] == 0){
			n--;
			printf("%d\n", num[n]);
		}
		else{
			n++;
		}
	}
	return 0;
}