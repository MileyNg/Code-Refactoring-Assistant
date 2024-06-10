#include<stdio.h>

int main()
{
    long long int i,j,n,count=0,k;
    while(scanf("%lld",&n)!=EOF)
    {
        for(i=2;i<=n;i++)
        {
            k=0;
            for(j=1;j<i;j++)
            {
                if(i%j==0)
                {
                    k++;
                }
            }
            if(k==1)
                    count++;

        }
        printf("%lld\n",count);
        count=0;
    }
    return 0;
}