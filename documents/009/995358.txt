#include <stdio.h>
#include <math.h>
#include <stdlib.h>

unsigned long long pow10(int n) {
    unsigned long long x;
    for (x = 1; n--;) {
        x *= 10;
    }
    return x;
}

int is_prime(unsigned long long x) {
    unsigned long long i, l;
    for (i = 3, l = sqrt(x) + 1; i < l; i += 2) {
        if (x % i == 0) return 0;
    }
    return 1;
}

long long find_number(int n, int c) {
    unsigned long long i, l, x, d;
    if (c < 0) {
        if (n == 1) {
            return 11;
        }
        else {
            return pow10(n * 2) - 1;
        }
    }

    for (i = pow10(2 * n + 1) - 1, l = pow10(2 * n);
         i > l; i -= 2) {
        for (x = i, d = pow10(2 * n);
             d > 1; x = (x%d)/10, d /= 100) {
            if (x / d != x % 10) break;
        }
        if (d == 1 && x == c && is_prime(i)) {
            return i;
        }
    }
    return pow10(n * 2 + 1) - 1;
}


int main(void) {
    int n, c, i;
    while (scanf("%d%d", &n, &c) == 2 && n) {
        if (n < 10) {
            printf("%llu\n", find_number(n, c));
        }
        else {
            printf("%llu%llu\n", find_number(n / 2, c), find_number(n / 2, c));
        }
    }
    return 0;
}