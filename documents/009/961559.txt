#include <stdio.h>
int main (void)
{
    int j,i,l[1000],a[1000],b;
    for(i=0;;i++)
    {
        if(scanf("%d",&a[i])==EOF)break;
        else if(a[i]==0)
        {
            printf("%d\n",a[i-1]);
                i--;
                i--;
        }
    }
    return 0;
}