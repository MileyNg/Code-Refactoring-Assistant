#include<stdio.h>
#include<math.h>
#define TRUE 1
#define FALSE 0
#define POWER_NUM 2
int func_cal(int a, int b, int c);
void func_output(int r);
int func_cal(int a, int b, int c)
{
	int num_a = 0, num_b = 0, num_c = 0;
	num_a = pow(a, POWER_NUM);
	num_b = pow(b, POWER_NUM);
	num_c = pow(c, POWER_NUM);
	
	if((num_a + num_b) == num_c)
	{
		return TRUE;
	}
	else if((num_a + num_c) == num_b)
	{
		return TRUE;
	}
	else if((num_c + num_b) == num_a)
	{
		return TRUE;
	}
	else
	{
		return FALSE;
	}
}
void func_output(int r)
{
	if(r == 1)
	{
		puts("YES");
	}
	else
	{
		puts("NO");
	}
}
main()
{
	int a = 0, b = 0, c = 0, n = 0, i = 0, result = 0;
	scanf("%d", &n);
	while(i < n)
	{
		scanf("%d %d %d", &a, &b, &c);
		result = func_cal(a, b, c);
		func_output(result);
		i++;
	}
	return 0;
}