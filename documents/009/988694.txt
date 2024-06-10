#include <stdio.h>

int gcd(int a, int b);

int main(void)
{
	int a, b;
	while (scanf("%d %d", &a, &b) != EOF){
		if (a < b){
			a ^= b;
			b ^= a;
			a ^= b;
		}

		printf("%d %d\n", gcd(a, b), (a / gcd(a, b)) * b);
	}

	return (0);
}

int gcd(int a, int b)
{
	if (a % b == 0){
		return (b);
	}

	return (gcd(b, a % b));
}