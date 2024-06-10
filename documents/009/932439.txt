#include <stdio.h>

int main(void)
{
    int a, b, c;

    scanf(" %d %d %d", &a, &b, &c);

    if (a > b){
        a ^= b;
        b ^= a;
        a ^= b;
    }
    if (b > c){
        b ^= c;
        c ^= b;
        b ^= c;
    }
    if (a > b){
        a ^= b;
        b ^= a;
        a ^= b;
    }

    printf("%d %d %d\n", a, b, c);

    return 0;
}