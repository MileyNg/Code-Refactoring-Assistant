#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define STACK 1000
#define compile 0
#define PandM 5
#define pop 4
void func_move(char input[], char mountain[][STACK]);
void func_pop(char input[], char mountain[][STACK], char result[]);
void func_push(char input[], char mountain[][STACK]);
void func_output(char result[]);
void func_init(char array[], int n) //初期化関数
{
#if compile == 1
	printf("func_init execution.\n");
#endif
	int i = 0;
	while(i < n)
	{
		array[i] = 0x00;
		i++;
	}
}
void func_init2(char array[][STACK], int n)
{
	int i = 0, j = 0;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < STACK; j++)
		{
			array[i][j] = 0x00;
		}
	}
}
void func_stacking(int n, char result[])
{
#if compile == 1
	printf("func_stacking execution.\n");
#endif
	char input[10];
	func_init(input, 10); //入力配列の初期化
	char mountain[n][STACK];
	int i = 0;
	func_init2(mountain, n);
	while(strcmp(input, "quit") != 0) //quit入力で終了
	{
		if((input[0] == 0x70) && (input[4] == 0x20)) //pushの判断条件
		{
			func_push(input, mountain);
#if compile == 1
			printf("return func_stacking.\n");
#endif
		}
		else if(input[3] == 0x20) //popの判断条件
		{
			func_pop(input, mountain, result);
#if compile == 1
			printf("return func_stacking.\n");
#endif
		}
		else if(input[0] == 0x6d) //moveの判断条件
		{
			func_move(input, mountain);
#if compile == 1
			printf("return func_stacking.\n");
#endif
		}
		func_init(input, 10);
#if compile == 1
		printf("input command.\n");
#endif
		gets(input);
	}
	func_output(result);
}
void func_push(char input[], char mountain[][STACK])
{
#if compile == 2
	printf("func_push exexcution.\n");
#endif
	int i = PandM, x = 0;
	char block;
	char num[3];
	func_init(num, 3);
	while(1)
	{
		if((0x30 <= input[i]) && (0x39 >= input[i]))
		{
			num[x] = input[i];
			x++;
			i++;
		}
		else if(0x00 == input[i])
		{
			block = input[i - 1];
#if compile == 2
			printf("1stroop break @ func_push.\n");
			printf("block = %c\n", block);
#endif
			break;
		}
		else
		{
			i++;
		}
	}
	x = atoi(num);
	x--;
	i = 0;
	while(1)
	{
		if(0x00 == mountain[x][i])
		{
			mountain[x][i] = block;
#if compile == 2
			printf("2ndroop break @ func_push.\n");
			printf("mountain[%d][%d] = %x\n", x, i, mountain[x][i]);
#endif			
			break;
		}
		else
		{
			i++;
		}
	}
}
void func_pop(char input[], char mountain[][STACK], char result[])
{
	int i = pop, j = 0, x = 0;
	char num[3];
	while(1)
	{
		if((0x30 <= input[i]) && (0x39 >= input[i]))
		{
			num[x] = input[i];
			x++;
			i++;
		}
		else
		{
			break;
		}
	}
#if compile == 3
	printf("1st roop break @ func_pop.\n");
	i = 0;
	while(num[i] != 0x00)
	{
		printf("num[%d] = %c\n", i, num[i]);
		i++;
	}
#endif
	x = atoi(num);
	x--;
	i = 0;
	while(1)
	{
		if(0x00 == mountain[x][i + 1])
		{
#if compile == 3
			printf("2nd roop break @ func_pop.\n");
			printf("mountain[%d][%d] = %d\n", x, i, mountain[x][i]);
#endif
			break;
		}
		else
		{
			i++;
		}
	}
	while(1)
	{
		if(0x00 == result[j])
		{
			result[j] = mountain[x][i];
			mountain[x][i] = 0x00;
#if compile == 3
			printf("3rd roop break @ func_pop.\n");
			printf("result[%d] = %d\n", j, result[j]);
			printf("mountain[%d][%d] = %d", x, i, mountain[x][i]);
#endif
			break;
		}
		else
		{
			j++;
		}
	}
}
void func_move(char input[], char mountain[][STACK])
{
	int i = PandM, j = 0, x = 0, y = 0;
	char num1[3], num2[3];
	func_init(num1, 3);
	func_init(num2, 3);
	while(1)
	{
		if((0x30 <= input[i]) && (0x39 >= input[i]))
		{
			num1[x] = input[i];
			x++;
			i++;
		}
		else
		{
			i++;
#if compile == 4
			printf("1st roop break @ func_move.\n");
			int debug1 = 0;
			while(num1[debug1] != 0x00)
			{
				printf("num1[%d] = %c\n", debug1, num1[debug1]);
				debug1++;
			}
#endif
			break;
		}
	}
	while(1)
	{
		if((0x30 <= input[i]) && (0x39 >= input[i]))
		{
			num2[y] = input[i];
			y++;
			i++;
		}
		else
		{
#if compile == 4
			printf("2nd roop break @ func_move.\n");
			int debug2 = 0;
			while(num2[debug2] != 0x00)
			{
				printf("num2[%d] = %c\n", debug2, num2[debug2]);
				debug2++;
			}
			printf("input[%d] = %x\n", i - 1, input[i - 1]);
#endif
			break;
		}
	}
	x = 0;
	y = 0;
	x = atoi(num1);
	x--;
	y = atoi(num2);
	y--;
	i = 0;
	while(1)
	{
		if(0x00 == mountain[x][i + 1])
		{
#if compile == 4
			printf("3rd roop break @ func_move\n");
			printf("code mountain[%d][%d] = %x\n", x, i, mountain[x][i]);
#endif
			break;
		}
		else
		{
			i++;
		}
	}
	while(1)
	{
		if(0x00 == mountain[y][j])
		{
			mountain[y][j] = mountain[x][i];
#if compile == 4
			printf("4th roop break @ func_move\n");
			printf("code mountain[%d][%d] = %x\n", y, j, mountain[y][j]);
#endif
			break;
		}
		else
		{
			j++;
		}
	}
	mountain[x][i] = 0x00;
	
}
void func_output(char result[])
{
	
	int i = 0;
#if compile == 1
	printf("func_output execution.\n");
#endif
	while(result[i] != 0x00)
	{
		printf("%c\n", result[i]);
		i++;
	}
}
main()
{
	int n = 0;
	scanf("%d", &n);
	char result[STACK];
	func_init(result, STACK);
	func_stacking(n, result);
	return 0;
}