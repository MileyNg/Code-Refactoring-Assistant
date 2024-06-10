#include<stdio.h>
#include<math.h>

#define FIRST_PRIME 2
#define SECOND_PRIME 3
#define compile 0

short func_primeFound(long n);
void func_init(short array[], long n);
short func_primeCount(short array[]);

main()
{
	long n = 0;
	short result = 0;
	while(scanf("%d", &n) != EOF)
	{
#if compile == 2
		printf("n = %d\n", n);
#endif
		result = func_primeFound(n);
#if compile == 2
		printf("result = ");
#endif
		printf("%d\n", result);
		n = 0;
	}
	return 0;
}

short func_primeFound(long n)
{
	short counter_in_func = 0;
	long i = 5, j = 0;
	//n = sqrt(n); //nにnの平方根を整数値化したものを代入
	short array_prime[n];
	
	func_init(array_prime, n);
	switch(n)
	{
	case 0:
	case 1:
		counter_in_func = 0;
		break;
	case 3:
	case 4:
		counter_in_func = 2;
		break;
	default:
		while(i <= n)
		{
#if compile == 2
			printf("i = %d\n", i);
#endif
			j = 0;
			while(array_prime[j] != 0)
			{
#if compile == 2
				printf("array_prime[%d] = %d\n", j, array_prime[j]);
#endif
				if(0 == (i % array_prime[j]))
				{
#if compile == 2
					printf("i = %d array_prime[%d] = %d\n", i, j, array_prime[j]);
					printf("break\n");
#endif
					break;
				}
				else if(0 != (i % array_prime[j]))
				{
					if(0 == array_prime[j + 1])
					{
						array_prime[j + 1] = i;
						counter_in_func++;
#if compile == 2
						printf("array_prime[%d] = %d\n", j, array_prime[j + 1]);
#endif
					}
					else
					{
						j++;
						continue;
					}
				}
			}
			i += 2;
		}
		counter_in_func += 2;
	}
	
	//counter_in_func = func_primeCount(array_prime);
	return counter_in_func;
}

void func_init(short array[], long n)
{
	long i = 2;
	array[0] = FIRST_PRIME; //2
	array[1] = SECOND_PRIME; //3
	while(i < n)
	{
#if compile == 2
		printf("i = %d\n", i);
#endif
		array[i] = 0;
		i++;
	}
}
/*
short func_primeCount(short array[])
{
	short i = 0;
	while(array[i] != 0)
	{
		i++;
	}
	return i;
}
*/
void trace(char str[], short n)
{
#if compile == 1
	printf("%s = %d\n", str, n);
#endif
}