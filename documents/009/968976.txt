#include <stdio.h>

int main(void)
{
	int a,b,c,p;
	
	scanf("%d %d %d",&a,&b,&c);
	
	if(a > b){
		p = a;
		a = b;
		b = p;
	}
	if(b > c){
		p = b;
		b = c;
		c = p;
	}
	if(a > b){
		p = a;
		a = b;
		b = p;
	}
	printf("%d %d %d\n",a,b,c);
	
	return 0;
}