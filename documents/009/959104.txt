#include<stdio.h>

int main()
{
     int i,j,k,n,count=0;
     while(scanf("%d",&n)!=EOF){
    for(i=2;i<=n;i++)
    {
        k=0;
        for(j=2;j<=i/2;j++)
        {
            if(i%j==0)
            {
                k++;
                break;
            }
            else
                continue;
        }
         if(k==0)
    {
        count++;
    }
}

      printf("%d\n",count);
      count=0;

     }


    return 0;
}