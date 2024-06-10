#include<stdio.h>
 
int risi(int);
int main(void)
{
	int week,syakkin;

	scanf("%d",&week);
   
	syakkin=risi(week);
	printf("%d\n",syakkin);
	return 0;
}

int risi(int n)
{
	int amari,price;
	if(n == 0)
		return 100000;
	else 
		price = (risi(n-1)*1.05);
		amari = price % 1000;
		if(amari > 0){
			price = ((price / 1000) + 1) * 1000;
		}
		return price;
}