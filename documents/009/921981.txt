
#include <stdio.h>

int main(void)
{
	int number,i,j,k,l,count=0;

	while(scanf("%d",&number) != EOF)
	{
		for(i=0;i<10;i++)
		{
			for(j=0;j<10;j++)
			{
				for(k=0;k<10;k++)
				{
					for(l=0;l<10;l++)
					{
						if(i + j + k + l == number) count++;
					}
				}
			}
		}
		printf("%d\n",count);
		count = 0;
	}
	return 0;
}