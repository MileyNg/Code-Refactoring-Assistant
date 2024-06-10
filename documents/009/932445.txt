#include <stdio.h>

void XORSwap(int *x, int *y)
{
    *x ^= *y;
    *y ^= *x;
    *x ^= *y;
}

int main(void)
{
    int a, b, c;
    
    scanf(" %d %d %d", &a, &b, &c);

    if (a > b){
        XORSwap(&a, &b);
    }
    if (b > c){
        XORSwap(&b, &c);
    }
    if (a > b){
        XORSwap(&a, &b);
    }

    printf("%d %d %d\n", a, b, c);

    return 0;
}