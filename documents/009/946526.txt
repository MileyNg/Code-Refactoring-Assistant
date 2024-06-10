#include <stdio.h>

int main(void)
{
	int a, b;
	int keta;
	int num;
	
	num = 0;
	
	while (scanf("%d %d", &a, &b) != EOF){
		keta = 0;
		num = a + b;
		while (num > 0){
			num /= 10;
			keta++;
		}
		
		printf("%d\n", keta);
	}
	
	return (0);
}