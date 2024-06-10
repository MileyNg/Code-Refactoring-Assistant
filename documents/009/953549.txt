#include <stdio.h>

int main(void)
{
	int a, b;
	int num;
	int keta;
	
	while (scanf("%d %d", &a, &b) != EOF){
		num = a + b;
		keta = 0;
		while (num > 0){
			num /= 10;
			keta++;
		}
		printf("%d\n", keta);
	}
	return (0);
}
			
	
	