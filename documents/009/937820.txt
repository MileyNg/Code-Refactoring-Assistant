#include <stdio.h>

int main(void)
{
	int n;
	int money;
	int i;
	
	scanf("%d", &n);
	
	money = 100000;
	for (i = 0; i < n; i++){
		money += money * 0.05;
		if (money % 1000 > 0){
			money /= 1000;
			money *= 1000;
			money += 1000;
		}
	}
	printf("%d\n", money);
	
	return (0);
}