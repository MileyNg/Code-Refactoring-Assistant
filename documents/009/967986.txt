#include <stdio.h>

int main(void){
	double pr = 10.0;
	int debt;
	int wk;
	while(scanf("%d", &wk) != EOF){
		debt = (int)(pr*(100 + 5*wk)/100 + 0.5)*10000;
		printf("%d\n", debt);
	}
	
	return 0;
}