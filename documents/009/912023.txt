#include <stdio.h>

int main(void) {
	int n,i,debt=100000;
	scanf("%d",&n);
	while (n--){
		debt=(debt*105/100+999)/1000*1000;
	}
	printf("%d\n",debt);
	return 0;
}