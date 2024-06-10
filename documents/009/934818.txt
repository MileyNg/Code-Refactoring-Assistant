#include <stdio.h>

int gcd(int a, int b);
int lcm(int a, int b);

int main(void)
{
	int s_gcd, s_lcm;
	int a, b;
	
	while (scanf("%d %d", &a, &b) != EOF){
	
		s_gcd = gcd(a, b);
		s_lcm = lcm(a, b);
		
		printf("%d %d\n", s_gcd, s_lcm);
	}
	return (0);
}

int gcd(int m, int n)
{
    int tmp;
	
	if (m < n){
		tmp = m;
		m = n;
		n = tmp;
	}
	
	while (n != 0){
		tmp = n;
		n = m % n;
		m = tmp;
	}
	
	return (m);
}

int lcm(int a, int b)
{
	return (a / gcd(a, b) * b);
}