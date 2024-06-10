#include<stdio.h>
int main()
{
    int combi(int n);
    int n;
    int result;
    while (scanf("%d",&n) != EOF)
    {
        if(n>37)
        {
            result = 0;
        }
        else
        {
             result = combi(n);
        }

        printf("%d\n",result);
    }
	return 0;
}

int combi(n)
{
    int a,b,c,d;
    int count;
    count = 0;
    for (a=0;a<10;a++)
        for(b=0;b<10;b++)
            for(c=0;c<10;c++)
                for(d=0;d<10;d++)
        {
            if(a+b+c+d == n)
                count++;
        }
        return count;



}