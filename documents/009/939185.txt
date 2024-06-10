#include <stdio.h>

void getprimes(unsigned long list[], int top){
	unsigned long i, j;
	int index;
	char tmp[top];

	for(i=0;i<top;i++) {
		tmp[i] = 1;
	}
	
	tmp[0] = tmp[1] = 0;
	for(i=2;i<top;i++) {
		if(tmp[i] == 1) {
			/* 素数 */
			list[index] = i;
			index ++;
			for(j=2;j*i<top;j++) {
				tmp[j*i] = 0;
			}
		}
	}

	list[index] = -1L;
}

#define PRIME_MAX 1000000

int main(void) {
	int i, c;
	unsigned long n;
	unsigned long primes[100000];
	getprimes(primes, PRIME_MAX);
	
	while(scanf("%d\n", &n) == 1) {
		c = 0;
		for(i=0;primes[i]!=-1L;i++) {
			if(primes[i] > n) break;

			c++;
		}
		printf("%d\n", c);
	}
	
	return 0;
}