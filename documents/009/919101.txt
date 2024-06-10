#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
    long long int n,m,j,k,l,i;
    while(scanf("%lld%lld",&n,&m)==2)
    {
        k=0;
        j=n+m;
        for(i=j;i>=1;i/=10)
            k++;
            printf("%lld\n",k);
    }
    return 0;
}