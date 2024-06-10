#include<stdio.h>
int countDigit(int a)
{
	int ret=0;
	while(a>0){ret++;a/=10;}
	return ret;
}

int main()
{
	int a,b;
	while(scanf("%d %d",&a,&b)!=EOF){
		printf("%d\n",countDigit(a+b));	
	}
	return 0;
}