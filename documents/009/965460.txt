#include<stdio.h>
#include<string.h>

#define WORD_MAX 31
#define DATASET_MAX 100

void initialize_c(char array[][WORD_MAX], int y, int x);
void initialize_d(int array[][DATASET_MAX], int y, int x);
void sorting(char w[][WORD_MAX], int p[][DATASET_MAX], int n);
void moving(char w[][WORD_MAX], int p[][DATASET_MAX], int n);
void bubble(int p[], int n);
void output(char w[][WORD_MAX], int p[][DATASET_MAX], int n);

main()
{
	int n = 0; //入力回数をカウント
	char word[DATASET_MAX][WORD_MAX];
	int page[DATASET_MAX][DATASET_MAX];
	initialize_c(word, DATASET_MAX, WORD_MAX); //char型配列の初期化
	initialize_d(page, DATASET_MAX, DATASET_MAX); //int型配列の初期化
	while(scanf("%s %d", word[n], &page[n][0]) != EOF)
	{
		n++;
	}
	sorting(word, page, n);
	moving(word, page, n);
	output(word, page, n);
	return 0;
}
void initialize_c(char array[][WORD_MAX], int y, int x)
{
	int i = 0, j = 0;
	for(i = 0; i < y; i++)
	{
		for(j = 0; j < x; j++)
		{
			array[i][j] = 0x00; //ヌル文字を代入
		}
	}
}
void initialize_d(int array[][DATASET_MAX], int y, int x)
{
	int i = 0, j = 0;
	for(i = 0; i < y; i++)
	{
		for(j = 0; j < x; j++)
		{
			array[i][j] = 1001; //page番号は1000まで
		}
	}
}
void sorting(char w[][WORD_MAX], int p[][DATASET_MAX], int n)
{
	int i = 0, j = 0;
	char temp_c[WORD_MAX]; //入れ替え用(char型)
	for(i = 0; i < WORD_MAX; i++) //初期化
	{
		temp_c[i] = 0x00;
	}
	int temp_d = 0; //入れ替え用(int型)
	/*
	for(i = 0; i < n; i++)
	{
		printf("w[%d] = %s p[%d] = %d\n", i, w[i], i, p[i][0]);
	}
	*/
	for(i = 0; i < n; i++)
	{
		for(j = i + 1; j < n; j++)
		{
			if(strcmp(w[j], w[i]) < 0)
			{
				strcpy(temp_c, w[i]); //文字列の入れ替え
				strcpy(w[i], w[j]);
				strcpy(w[j], temp_c);
				temp_d = p[i][0]; //ページ場号の入れ替えも同時に行う
				p[i][0] = p[j][0];
				p[j][0] = temp_d;
			}
		}
	}
	/*
	for(i = 0; i < n; i++)
	{
		printf("w[%d] = %s p[%d] = %d\n", i, w[i], i, p[i][0]);
	}
	*/
}
void moving(char w[][WORD_MAX], int p[][DATASET_MAX], int n)
{
	int i = 0, j = 0, k = 0;
	for(i = 0; i < n; i++)
	{
		for(j = i + 1; j < n; j++)
		{
			if(strcmp(w[i], "\0") == 0)
			{
				break;
			}
			if(strcmp(w[i], w[j]) == 0)
			{
				k++;
				p[i][k] = p[j][0];
				strcpy(w[j], "\0"); //ヌル文字代入
			}
		}
		k = 0;
	}
}
void bubble(int p[], int n)
{
	int temp = 0;
	int i = 0, j = 0;
	for(i = 0; p[i + 1] != 1001; i++)
	{
		for(j = i + 1; p[j] != 1001; j++)
		{
			if(p[i] > p[j])
			{
				temp = p[i];
				p[i] = p[j];
				p[j] = temp;
			}
		}
	}
}
void output(char w[][WORD_MAX], int p[][DATASET_MAX], int n)
{
	int i = 0, j = 0;
	for(i = 0; i < n; i++)
	{
		if(strcmp(w[i], "\0") == 0)
		{
			//printf("continue\n");
			continue;
		}
		else
		{
			printf("%s\n", w[i]);
			bubble(p[i], n);
			for(j = 0; p[i][j] != 1001; j++)
			{
				if(p[i][j + 1] != 1001)
				{
					printf("%d ", p[i][j]);
				}
				else
				{
					printf("%d\n", p[i][j]);
				}
			}
		}
	}
}