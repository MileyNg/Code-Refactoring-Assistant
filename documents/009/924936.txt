#include<stdio.h>
#include<string.h>
#define LENGTH 101
#define compile 0

void initial(char str[][LENGTH], int n)
{
	int i = 0, j = 0;
	
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < LENGTH; j++)
		{
			str[i][j] = 0x00;
			
			#if compile == 1
			printf("str[%d][%d] = 0x%x\n", i, j, str[i][j]);
			#endif
		}
	}
}

int count(char str_t[][LENGTH], char str_h[][LENGTH], int *c_t, int *c_h, int t)
{
	int i = 0;
	
	#if compile == 2
	printf("begin i-roop %d in function count\n", i);
	#endif
	
	if(str_t[t][i] == str_h[t][i])
	{
		for(i = 1; i < LENGTH; i++)
		{
			if((str_t[t][i] > str_h[t][i]) || ((str_t[t][i] != 0x00) && (str_h[t][i] == 0x00)))
			{
				*c_t += 3;
				#if compile == 2
				printf("c_t++; done\nc_t = %d\n", *c_t);
				#endif
				return 0;
			}
			else if((str_h[t][i] > str_t[t][i]) || ((str_t[t][i] == 0x00) && (str_h[t][i] != 0x00)))
			{
				*c_h += 3;
				#if compile == 2
				printf("c_h++; done\nc_h = %d\n", *c_h);
				#endif
				return 0;
			}
			else if(str_t[t][i] == str_h[t][i])
			{
				if((str_t[t][i + 1] == 0x00) && (str_h[t][i + 1] == 0x00))
				{
					*c_t += 1;
					*c_h += 1;
					#if compile == 2
					printf("c_t = %d", *c_t);
					printf(" c_h = %d\n", *c_h);
					#endif
					return 0;
				}
				
				#if compile == 2
				printf("str_t[%d][%d] == str_h[%d][%d]\n", t, i, t, i);
				puts("done continue;");
				#endif
				
				continue;
			}
		}
	}
	else if(str_t[t][i] > str_h[t][i])
	{
		*c_t += 3;
		#if compile == 2
		printf("c_t++; done\nc_t = %d\n", *c_t);
		#endif
		return 0;
	}
	else if(str_h[t][i] > str_t[t][i])
	{
		*c_h += 3;
		#if compile == 2
		printf("c_h++; done\nc_h = %d\n", *c_h);
		#endif
		return 0;
	}
	
}

main()
{
	int n = 0, counter_t = 0, counter_h = 0, counter_turn = 0;
	int i = 0, j = 0, k = 0;
	
	scanf("%d", &n);
	
	#if compile == 2
	printf("n = %d\n", n);
	#endif
	
	char taro_card[n][LENGTH];
	char hanako_card[n][LENGTH];
	
	initial(taro_card, n);
	initial(hanako_card, n);
	
	#if compile == 1
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < LENGTH; j++)
		{
			printf("taro_card[%d][%d] = 0x%x\n", i, j, taro_card[i][j]);
		}
	}
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < LENGTH; j++)
		{
			printf("hanako_card[%d][%d] = 0x%x\n", i, j, hanako_card[i][j]);
		}
	}
	#endif
	
	for(i = 0; i < n; i++) //入力、関数呼び出しループ
	{
		#if compile == 2
		printf("begin i-roop %d\n", i);
		puts("input taro's card & hanako's card");
		#endif
		
		scanf("%s %s", taro_card[i], hanako_card[i]);
		
		#if compile == 2
		printf("taro_card[%d] = %s\n", i, taro_card[i]);
		printf("hanako_card[%d] = %s\n", i, hanako_card[i]);
		#endif
		
		//ここで関数呼び出し
		count(taro_card, hanako_card, &counter_t, &counter_h, counter_turn);
		counter_turn++;
	}
	
	#if compile == 2
	printf("taro hanako = ");
	#endif
	
	printf("%d %d\n", counter_t, counter_h);
	
	return 0;
}