#include<stdio.h>
main()
{
    long long int a,b,sum=0,i,j;
    while(scanf("%lld%lld",&a,&b)==2)
    {
        sum=a+b;
        j=0;
        while(sum!=0)
        {
            sum/=10;
            j++;
        }
        printf("%lld\n",j);
    }
    return 0;
}