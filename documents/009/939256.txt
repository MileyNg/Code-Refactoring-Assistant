#include <stdio.h>

int main(void)
{
	long long int num1, num2, remainder, numerator, denominator;
	long long int gcd, lcm;
	
	while(scanf("%lld %lld\n", &num1, &num2) == 2) {
		if (num1 > num2) {
			numerator = num1;
			denominator = num2;
		} else {
			numerator = num2;
			denominator = num1;
		}
		remainder = num1 % num2;
		while(remainder !=0) {
			numerator = denominator;
			denominator = remainder;
			remainder = numerator % denominator;
		}
		gcd = denominator;
		lcm = num1 / gcd * num2;

		printf("%lld %lld\n", gcd, lcm);
	}
	return 0;
}