#include<stdio.h>

#define NUM 0
#define APIECE 1 //単価
#define QUANT 2 //数量
#define RESULT 3 //販売実績

void initialize(int array[][4], int n);
void calculate(int array[][4], int n);
void output(int array[][4], int n);

main()
{
	int n = 0, i = 0;
	while(scanf("%d", &n), (n != 0))
	{
		//scanf("\n");
		//printf("n = %d\n", n);
		int menber[n][4];
		initialize(menber, n);
		for(i = 0; i < n; i++)
		{
			scanf("\n");
			scanf("%d %d %d", &menber[i][NUM], &menber[i][APIECE], &menber[i][QUANT]);
		}
		/*
		int j = 0;
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < 4; j++)
			{
				printf("%d ", menber[i][j]);
			}
			puts("");
		}
		*/
		calculate(menber, n);
		output(menber, n);
	}
	
	return 0;
}
void initialize(int array[][4], int n)
{
	int i = 0, j = 0;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < 4; j++)
		{
			array[i][j] = 0;
		}
	}
}
void calculate(int array[][4], int n)
{
	int i = 0, j = 0;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < array[i][QUANT]; j++)
		{
			array[i][RESULT] += array[i][APIECE];
			if(array[i][RESULT] >= 1000000)
			{
				break;
			}
		}
	}
	for(i = 0; i < n; i++)
	{
		for(j = i + 1; j < n; j++)
		{
			if(array[i][NUM] == array[j][NUM])
			{
				array[i][RESULT] += array[j][RESULT];
				array[j][RESULT] = 0;
			}
		}
	}
	/*
	for(i = 0; i < n; i++)
	{
		printf("array[%d][NUM] = %d array[%d][RESULT] = %d\n", i, array[i][NUM], i, array[i][RESULT]);
	}
	*/
}
void output(int array[][4], int n)
{
	int i = 0, flag = 0;
	for(i = 0; i < n; i++)
	{
		if(1000000 <= array[i][RESULT])
		{
			printf("%d\n", array[i][NUM]);
			flag++;
		}
	}
	if(flag == 0)
	{
		printf("NA\n");
	}
}