#include <stdio.h>

int main(void)
{
	int array[3];
	int i, j, tmp;
	scanf("%d %d %d", &array[0], &array[1], &array[2]);

	for (j = 3; j > 0; j--) {
		for (i = 0; i < j - 1; i++) {
			if (array[i] > array[i + 1]) {
				tmp = array[i];
				array[i] = array[i + 1];
				array[i + 1] = tmp;
			}
		}
	}

	printf("%d %d %d\n", array[0], array[1], array[2]);
	return 0;
}