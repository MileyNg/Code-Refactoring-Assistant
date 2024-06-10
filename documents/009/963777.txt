#include<stdio.h>
#include<string.h>

#define MAX 1001

void initialize(char array[], int n);
void judge(char input[], char target[]);

main()
{
	char input[MAX];
	char target[7] = {'H','o','s','h','i','n','o'};
	initialize(input, MAX);
	int i = 0, n = 0;
	scanf("%d\n", &n);
	for(i = 0; i < n; i++)
	{
		gets(input);
		judge(input, target);
		printf("%s\n", input);
		initialize(input, MAX);
	}
	return 0;
}
void initialize(char array[], int n)
{
	short i = 0;
	for(i = 0; i < MAX; i++)
	{
		array[i] = 0x00;
	}
}
void judge(char input[], char target[])
{
	short i = 0, j = 0;
	for(i = 0; input[i] != 0x00; i++)
	{
		if(input[i] == target[0])
		{
			for(j = 0; j < 7; j++)
			{
				if((j < 5) && (input[i + j] != target[j]))
				{
					break;
				}
				else if((j == 6) && (input[i + j] == 'o'))
				{
					input[i + j] = 'a';
				}
			}
		}
	}
}