#include  <stdio.h>
#include <stdlib.h>

int main(void)
{
	int number,*values,i,j,max,sum;

	scanf("%d",&number);

	while(number != 0)
	{
		values = (int *)malloc(sizeof(int) *number);
		max = -100001;
		for(i = 0;i < number ; i++)
		{
			scanf("%d",&values[i]);
		}

		for(i = 0;i<number ; i++)
		{
			sum = 0;
			for( j = i; j < number ;j++)
			{
				sum += values[j];
				if(max < sum)
				{
					max = sum;
				}
			}
		}

		printf("%d\n",max);
		scanf("%d",&number);
	}

	return 0;
}