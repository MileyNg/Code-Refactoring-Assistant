#include <stdio.h>

int main(void){
	int _array[100];
	int i, n;
	scanf("%d", &n);
	i = n;
	while (i--)
		scanf("%d", &_array[i]);
	for (i = 0; i < n ; i++){
		if (i) printf(" ");
		printf("%d", _array[i]);
	}
	printf("\n");
	return 0;
}