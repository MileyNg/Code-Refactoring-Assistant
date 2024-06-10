#include <stdio.h>
 
#define PRIME_MAX 1000000
int getprimes(int list[], int top){
    int i, j;
    int index = 0;
    char tmp[PRIME_MAX];
 
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
 
    list[index] = -1;
    return index;
}
 
int gcd(int a, int b) {
	if (a < 0 || b < 0) {
		return 0;
	}

	while (b > 0) {
		int c = a % b;
		a = b;
		b = c;
	}

  return a;
}

inline int numofbits5(long bits) {
    bits = (bits & 0x55555555) + (bits >> 1 & 0x55555555);
    bits = (bits & 0x33333333) + (bits >> 2 & 0x33333333);
    bits = (bits & 0x0f0f0f0f) + (bits >> 4 & 0x0f0f0f0f);
    bits = (bits & 0x00ff00ff) + (bits >> 8 & 0x00ff00ff);
    return (bits & 0x0000ffff) + (bits >>16 & 0x0000ffff);
}

int main(void) {
    int i;
    int n, base;
    int size;
    int *primes;
    int div[1000];
    int d;
    int j;
    int old_prime = -1;
	unsigned char* memo;
	double c;
    primes = (int*)malloc(100001*4);
    size = getprimes(primes, PRIME_MAX);
    
    scanf("%d\n", &base);
    i = d = 0;
    n = base;
    while(n > 1) {
        if((n % primes[i]) == 0) {
        	if(old_prime != primes[i]) {
	            div[d] = primes[i];
	            d++;
        	}
            n /= primes[i];
            old_prime = primes[i];
        } else {
            i++;
        }
         
        if(i >= size) {
            div[d] = n;
            d++;
            break;
        }
    }
    free(primes);

	c = base;
	for(j=0;j<d;j++) {
		c = c * (1 - 1.0/div[j]);
	}
/*
    memo = (unsigned char*)malloc(base/8+1);
    for(i=0;i<base/8+1;i++) memo[i] = 0;
	c = 0;
    for(j=0;j<d;j++) {
        for(i=div[j];i<base;i+=div[j]) {
        	memo[i/8] |= 1<<(i%8);
        }
    }
    
    for(i=1;i<base;i++) {
    	if(!(memo[i/8]&(1<<(i%8)))) c++;
    }
*/
    printf("%d\n", (int)c);
    
    return 0;
}