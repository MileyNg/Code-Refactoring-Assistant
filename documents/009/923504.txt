#include <stdio.h>

int GCD(int a, int b)
{
	if (b == 0){
		return a;
	}
	else {
		return GCD(b, a % b);
	}
}
int LCM(int a, int b, int gcd)
{
	return a / gcd * b;
}

int main(void)
{
	int a, b;
	int gcd, lcm;
	
	while (scanf("%d %d", &a, &b) != EOF){
		if (a < b){
			int tmp = a;
			a = b;
			b = tmp;
		}
		gcd = GCD(a, b);
		lcm = LCM(a, b, gcd);
		printf("%d %d\n", gcd, lcm);
	}
	
	return 0;
}