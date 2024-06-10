// AOJ
#include<stdio.h>

int main(){
	int n, x = 100000;
	scanf("%d", &n);
	for(; n > 0; n--){
		x += x/20;
		if(x%1000 != 0){
			x = (x/1000+1)*1000;
		}
	}
	printf("%d\n", x);

	return 0;
}