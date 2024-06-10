#include <stdio.h>

int main(void)
{
	int a, b, c;
	int i;
	
	while(scanf("%d %d", &a, &b) != EOF){
		c = a + b;
		for (i=1; (c/=10) > 0;i++ ){}
		printf("%d\n", i);
	}
	
	return(0);
}