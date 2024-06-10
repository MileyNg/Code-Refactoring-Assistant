#include <stdio.h>
#include <stdlib.h>

int main()
{
    long long int a, b, c;
    while(scanf("%lld%lld", &a, &b)!=EOF)
    {
        c = a + b;
        if(c<10)
        {
            printf("1\n");
        }
        else if(c>9 && c<100)
        {
            printf("2\n");
        }
        else if(c>99 && c<1000)
        {
            printf("3\n");
        }
        else if(c>999 && c<10000)
        {
            printf("4\n");
        }
        else if(c>9999 && c<100000)
        {
            printf("5\n");
        }
        else if(c>99999 && c<1000000)
        {
            printf("6\n");
        }
        else if(c>999999 && c<10000000)
        {
            printf("7\n");
        }
    }
    return 0;
}