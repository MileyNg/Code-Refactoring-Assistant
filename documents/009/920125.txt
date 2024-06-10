#include<stdio.h>
int main()
{
    long int a,b,c,co=0;
    while(scanf("%ld%ld",&a,&b)!=EOF)
    {
        c=a+b;
         co=0;

        while(c>0)
        {
             c=c/10;
            co++;
        }
      printf("%ld\n",co);
    }
    return 0;
}