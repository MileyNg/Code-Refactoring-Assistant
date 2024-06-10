#include <stdio.h>
int main(void){
	int n, i, frac;
	float out;
	out = 100000;
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		out = out * 1.05;
		frac = (int)out % 1000;
		if(frac != 0) out = out - (float)frac + 1000;
	}
	printf("%d\n", (int)out);
	return 0;
}