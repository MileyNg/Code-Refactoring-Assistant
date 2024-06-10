#include<stdio.h>

int main(void)
{
	int n,i,g;
	int a[100];	
	scanf("%d",&n);
	for(i = 0;i < n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i = 0;i < n / 2;i++)
	{
		g = a[i];
		a[i] = a[n-1-i];
		a[n-1-i] = g;
	}
	for(i = 0;i < n;i++)
	{
		if(i != (n-1))
			printf("%d ",a[i]);
		else
			printf("%d\n",a[i]);
	}
	return 0;
}