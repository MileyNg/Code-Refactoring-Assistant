//ヘッダファイル
#include<stdio.h>

//マクロ定義
#define MAX 10000
#define FALSE 1
#define compile 1

//関数のプロトタイプ宣言
void func_init(int array[], int n);

main()
{
	int dead_end[MAX];
	int exit[MAX];
	func_init(dead_end, MAX);
	func_init(exit, MAX);
	int input = 0, i = 0, j = 0, k = 0, flag = 0;
	while(scanf("%d", &input) != EOF)
	{
		if(input != 0)
		{
			dead_end[i] = input; //現在のiを要素番号としてinputを入力
			i++;
		}
		else if(input == 0)
		{
			exit[j] = dead_end[--i];
			dead_end[i] = 0;
			j++;
		}
	}
	
	for(i = 0; exit[i] != 0; i++)
	{
		printf("%d\n", exit[i]);
	}
	return 0;
}
void func_init(int array[], int n)
{
	int i = 0;
	for(i = 0; i < n; i++)
	{
		array[i] = 0;
	}
}