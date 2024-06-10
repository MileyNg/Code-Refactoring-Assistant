#include <stdio.h>

int main(){

	int a=0,b=0,x=0;

	while (scanf("%d%d", &a, &b)!=EOF){
		
		if (a + b < 1000000){
			x=6;
		}else if(a + b < 100000){
			x=5;
		}else if (a + b < 10000){
			x=4;
		}else if (a + b < 1000){
			x=3;
		}else if (a + b < 100){
			x=2; 
		}else if (a + b < 10){
			x=1;
		}printf("%d\n", x);
	}
	return 0;
}