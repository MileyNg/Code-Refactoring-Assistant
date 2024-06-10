#include <stdio.h>

int main(void)
{
	int train;
	int a[10];
	int i;

	for (i = 0; i < 10; i++){
		a[i] = 0;
	}

	while (scanf("%d", &train) != EOF){
		if (train){
			for (i = 0; i < 10; i++){
				if (a[i] == 0){
					a[i] = train;
					break;
				}
			}
		}
		else {
			for (i = 9; i >= 0; i--){
				if (a[i] != 0){
					printf("%d\n", a[i]);
					a[i] = 0;
					break;
				}
			}
		}
	}

	return (0);
}