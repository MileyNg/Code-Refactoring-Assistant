#include<stdio.h>
#include<math.h>

void initialize(int array[], int n);
void diagonal(int array[]);
void process(int size, int hole[], int n);

main()
{
	int i = 0, n = 0, size[3];
	initialize(size, 3);
	while(scanf("%d %d %d", &size[0], &size[1], &size[2]), ((size[0] != 0) && (size[1] != 0) && (size[2] != 0)))
	{
		scanf("%d", &n);
		int hole[n];
		initialize(hole, n);
		for(i = 0; i < n; i++)
		{
			scanf("%d", &hole[i]);
		}
		diagonal(size);
		process(size[0], hole, n);
		initialize(size, 3);
	}
	
	return 0;
}
void initialize(int array[], int n)
{
	int i = 0;
	for(i = 0; i < n; i++)
	{
		array[i] = 0;
	}
}
void diagonal(int array[])
{
	int temp[3];
	initialize(temp, 3);
	int i = 0, j = 0;
	for(i = 0; i < 3; i++) //配列arrayを配列tempにコピー
	{
		temp[i] = array[i];
	}
	for(i = 0; i < 3; i++) //三平方の定理を使って対角線の長さを計算
	{
		j = i + 1;
		if(j == 3)
		{
			j = 0;
		}
		array[i] = sqrt(pow(temp[i], 2) + pow(temp[j], 2));
	}
	for(i = 0; i < 3; i++)
	{
		for(j = i + 1; j < 3; j++)
		{
			if(array[i] > array[j])
			{
				temp[0] = array[i];
				array[i] = array[j];
				array[j] = temp[0];
			}
		}
	}
}
void process(int size, int hole[], int n)
{
	int i = 0;
	for(i = 0; i < n; i++)
	{
		if(size < (hole[i] * 2))
		{
			printf("OK\n");
		}
		else
		{
			printf("NA\n");
		}
	}
}