#include <stdio.h>
#include <stdlib.h>

long long gcd(long long a, long long b){
	return b==0 ? a : gcd(b, a%b);
}

int main()
{
    long long a, b, g, l;
    while(scanf("%lld %lld", &a, &b)!=EOF){
        g = gcd(a,b);
        l = (a/g)*b;
        printf("%lld %lld\n", g, l);
    }
    return 0;
}