#include <stdio.h>
#include <math.h>

int main(void) {
	long a,b,i;
		
	while( scanf("%ld %ld", &a, &b) != EOF ) {
	
		long G=1,L=1;
	
		if(a<b) {
			long tmp = a;
			a = b;
			b = tmp;
		}
		
		G=a*b;
		//a>=bの状態
		
		while(b%2==0 && a%2==0) {
			L *= 2;
			b/=2;
			a/=2;
		}
		
		
		i=b;
		while(i > 2) {
			if(b%i==0 && a%i==0) {
					L *= i;
					b /= i;
					a /= i;
			}
			else i = i-2;
		}
		
		G /= L;
		
		printf("%ld %ld\n", L, G);
	}
	return 0;		
}	