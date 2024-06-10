#include<stdio.h>

#define NUMBER 10 //区分の数+1
#define TRAIN 3 //電車の数+1

void initialize(int array[], int n);
void sigma(int sum_division[], int division[], int n);
int judge(double r_time, int velocity, int sum_velocity[]);

main()
{
	int division[NUMBER];
	int sum_division[NUMBER - 1];
	int velocity[TRAIN];
	
	double running_time = 0;
	int result = 0;
	
	initialize(division, NUMBER);
	initialize(sum_division, NUMBER);
	initialize(velocity, TRAIN);
	
	while(scanf("%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d", &division[0], &division[1], &division[2], &division[3], &division[4], &division[5], &division[6], &division[7], &division[8], &division[9], &velocity[0], &velocity[1]) != EOF)
	{
		sigma(sum_division, division, NUMBER);
		velocity[2] = velocity[0] + velocity[1];
		//printf("velocity[2] = %d\n", velocity[2]); //デバッグ用
		running_time = (double)sum_division[9] / velocity[2];
		//printf("runnning_time = %lf\n", running_time); //デバッグ用
		result = judge(running_time, velocity[0], sum_division);
		printf("%d\n", result);
		
		initialize(division, NUMBER);
		initialize(sum_division, NUMBER);
		initialize(velocity, TRAIN);
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

void sigma(int sum_division[], int division[], int n)
{
	int i= 0;
	for(i = 0; i < n; i++)
	{
		if(i == 0)
		{
			sum_division[i] = division[i];
		}
		else
		{
			sum_division[i] = sum_division[i - 1] + division[i];
		}
		//printf("sum_division[%d] = %d\n", i, sum_division[i]); //デバッグ用
	}
}

int judge(double r_time, int velocity, int sum_division[])
{
	int i = 0, j = 0;
	double distance = 0;
	
	distance = (double)velocity * r_time;
	//printf("distance = %lf\n", distance); //デバッグ用
	for(i = 0; i < NUMBER; i++)
	{
		j = i + 1;
		//printf("i = %d j = %d\n", i, j); //デバッグ用
		if((sum_division[i] < distance) && (sum_division[j] >= distance))
		{
			return j + 1;
		}
	}
}