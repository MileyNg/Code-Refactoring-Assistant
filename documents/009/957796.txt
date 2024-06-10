#include<stdio.h>

#define NUMBER_IN 4
#define NUMBER_OUT 2
#define HIT 0
#define BLOW 1

void initialize(int array[]);
int check_hit(int array1[], int array2[]);
int check_blow(int array1[], int array2[]);

main()
{
	int input1[NUMBER_IN];
	int input2[NUMBER_IN];
	int result[NUMBER_OUT];
	
	initialize(input1); //初期化
	initialize(input2);
	result[HIT] = 0, result[BLOW] = 0;
	
	while(1)
	{
		//scanf("%d %d %d %d", &input1[0], &input1[1], &input1[2], &input1[3]);
		if(scanf("%d %d %d %d", &input1[0], &input1[1], &input1[2], &input1[3]) == EOF)
		{
			break;
		}
		scanf("%d %d %d %d", &input2[0], &input2[1], &input2[2], &input2[3]);
		
		result[HIT] = check_hit(input1, input2);
		result[BLOW] = check_blow(input1, input2);
		
		printf("%d %d\n", result[HIT], result[BLOW]);
		
		initialize(input1); //初期化
		initialize(input2);
		result[HIT] = 0, result[BLOW] = 0;
	}
	
	return 0;
}
void initialize(int array[])
{
	short i = 0;
	for(i = 0; i < NUMBER_IN; i++)
	{
		array[i] = 0;
	}
}
int check_hit(int array1[], int array2[])
{
	short i = 0, flag = 0;
	for(i = 0; i < NUMBER_IN; i++)
	{
		if(array1[i] == array2[i])
		{
			flag++;
		}
	}
	return flag;
}
int check_blow(int array1[], int array2[])
{
	short i = 0, j = 0, flag = 0;
	for(i = 0; i < NUMBER_IN; i++)
	{
		for(j = 0; j < NUMBER_IN; j++)
		{
			if((array1[i] == array2[j]) && (i != j))
			{
				flag++;
			}
		}
	}
	return flag;
}