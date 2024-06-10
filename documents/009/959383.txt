#include<stdio.h>
#include<math.h>

#define ELEMENT 11 //1023=512+256+128+64+32+16+8+4+2+1+制御用
#define BIN 2

void initialize(int array[], int n);
void integer_to_binary(int number, int array[]);
void calculate_weight(int array[]);

main()
{
	int input = 0, i = 0;
	int binary[ELEMENT]; //0or1が代入
	while(scanf("%d", &input) != EOF)
	{
		initialize(binary, ELEMENT);
		integer_to_binary(input, binary);
		calculate_weight(binary);
		input = 0;
	}
	
	return 0;
}

void initialize(int array[], int n)
{
	int i = 0;
	for(i = 0; i < n; i++)
	{
		array[i] = -1;
	}
}

void integer_to_binary(int number, int array[])
{
	static int quot = 0;
	static int i = 0;
	
	quot = number;
	array[i] = quot % BIN;
	i++;
	quot /= BIN;
	
	if(quot < 1)
	{
		i = 0;
		return;
	}
	else
	{
		integer_to_binary(quot, array);
	}
	
}
void calculate_weight(int array[])
{
	int sum = 0;
	int i = 0;
	for(i = 0; i < ELEMENT; i++)
	{
		if(array[i] == 1)
		{
			array[i] = pow(BIN, i);
		}
		//printf("array[%d] = %d\n", i, array[i]);
	}
	
	for(i = 0; i < ELEMENT; i++)
	{
		if((array[i + 1] == -1) && (array[i] > 0))
		{
			printf("%d\n", array[i]);
		}
		else if(array[i] > 0)
		{
			printf("%d ", array[i]);
		}
	}
	
}