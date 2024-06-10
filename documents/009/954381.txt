#include <stdio.h>
int main(void)
{
    int i,j,k,l,m,imput;
    m=0;

    while(scanf("%d",&imput)!=EOF)
    {
        for(i=0;i<10;i++)
        {
            for(j=0;j<10;j++)
            {
                for(k=0;k<10;k++)
                {
                    for(l=0;l<10;l++)
                    {
                        if(i+j+k+l==imput)
                        {
                            m++;
                        }
                    }
                }
            }
        }
        printf("%d\n",m);
        m=0;
    }

     return 0;
}