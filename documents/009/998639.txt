#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIEVE_SIZE 1000000

int sieve_idx, prime_idx;
char sieve[SIEVE_SIZE];

void init_prime_generator() {
    int i;
    sieve_idx = 2;
    prime_idx = 2;
    memset(sieve, 1, sizeof(sieve));
    sieve[0] = sieve[1] = 0;
}

void reset_prime_count() {
    prime_idx = 2;
}

int next_prime() {
    int i, j, dj;
    if (prime_idx < sieve_idx) {
        if (prime_idx == 2) {
            prime_idx = 3;
            return 2;
        }
        for (i = prime_idx; i < SIEVE_SIZE; i += 2) {
            if (sieve[i] == 1) {
                prime_idx = i + 2;
                return i;
            }
        }
    }
    if (sieve_idx < 3) {
        prime_idx = sieve_idx = 3;
        return 2;
    }
    for (i = sieve_idx; i < SIEVE_SIZE; i+=2) {
        if (sieve[i] == 1) {
            sieve_idx = i + 2;
            for (dj = i*2, j = i+dj; j < SIEVE_SIZE; j += dj) {
                sieve[j] = 0;
            }
            prime_idx = sieve_idx;
            return i;
        }
    }
    return 0;
}


int main (void) {
    int a, d, n;
    int i, k, p;

    init_prime_generator();

    while (scanf("%d%d%d", &a, &d, &n) != EOF && a && d && n) {
        reset_prime_count();
        p = 0;
        for (i = a, k = 0; i < SIEVE_SIZE ;i += d) {
            while (p < i) {
                p = next_prime();
            }
            if (i == p) {
                k++;
                if (k == n) break;
            }
        }
        printf("%d\n", p);
    }
    return 0;
}