#include <stdio.h>

#define MAX 1000000
int prime[MAX];

int main(void)
{
	int number, i, j, count;
	prime[0] = prime[1] = 0;
	for (i = 2; i < MAX; i++)
	{
		prime[i] = 1;
	}
	for (i = 2; i < 1001; i++)
	{
		if (prime[i])
		{
			for (j = 2 * i; j < MAX; j += i)
			{
				prime[j] = 0;
			}
		}
	}
	while (scanf("%d", &number) != EOF)
	{
		count = 0;
		for (i = 2; i <= number; i++)
		{
			count += prime[i];
		}
		printf("%d\n", count);
	}
  return 0;
}