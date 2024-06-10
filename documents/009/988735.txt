#include <stdio.h>

int main(void)
{
	int n;
	int ans = 100000;
	int i;

	scanf("%d", &n);

	for (i = 0; i < n; i++){
		ans *= 1.05;
		ans += 999;
		ans /= 1000;
		ans *= 1000;
	}

	printf("%d\n", ans);

	return (0);
}