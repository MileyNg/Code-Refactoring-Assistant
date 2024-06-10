#include<stdio.h>

int main()
{
    long long int x,y,z,count=0,count_1=1;
    while((scanf("%lld %lld",&x,&y))!=EOF)
    {
        if(x>=0&&y<=1000000)
        {
            z=x+y;
            //m=z;
            while(z!=0)
            {
                z=z/10;

                count++;
            }
            printf("%lld\n",count);

        }
         count=0;
        if(count_1>200)
            break;
            count_1++;
    }

    return 0;
}