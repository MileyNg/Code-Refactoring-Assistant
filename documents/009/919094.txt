#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int i, j, n, *a, max = 0;

	scanf("%d", &n);
	a = (int *) malloc(sizeof(int) * (n + 1));

	for (i = 1; i < n + 1; i++) {
		scanf("%d", &a[i]);
	}

	for (j = n; j > 0; j--) {
		for (i = j - 1; i > 0; i--) {
			if (max < (a[j] - a[i])) {
				max = a[j] - a[i];
			}
		}
	}

	printf("%d", max);

	return 0;
}