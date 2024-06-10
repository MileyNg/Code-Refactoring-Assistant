#include <stdio.h>

int main(void) {
	int a,b,c,i;
	int count;
	scanf("%d %d %d\n", &a, &b, &c);
	for(i=a,count=0;i<=b;i++) {
		if(c%i==0) count ++;
	}
	printf("%d\n", count);
	
	return 0;
}