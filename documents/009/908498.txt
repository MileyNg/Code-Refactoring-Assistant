#include<stdio.h>
int main()
{
	char c;
	int n;
	for(;;)
	{
		n=0;
		for(;~(c=getchar())&&c!=10;c>30?n+=(c-'0'):0);
		if(n==0)return 0;
		printf("%d\n",n);
	}
}