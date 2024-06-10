#include<stdio.h>
 
#define MAX 5000 //最大項数
 
void func_init(int array[], int n);
int func_cal(int array[], int n);
 
main()
{
    int n = 0, i = 0, sum_max = 0; //項数代入用変数n,ループ制御変数i,最大合計値代入変数sum_max
    while(1) //nが0でない限り
    {
    	scanf("%d", &n);
    	if(n == 0)
    	{
    		break;
    	}
        int numbers[n]; //入力された値をを代入する配列
        func_init(numbers, n); //配列の初期化
        for(i = 0; i < n; i++)
        {
            scanf("%d", &numbers[i]); //入力をnumbersのi番目に代入
        }
        sum_max = func_cal(numbers, n);
        printf("%d\n", sum_max);
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
int func_cal(int array[], int n)
{
    int i = 0, j = 0, temp = -100000;
    int max = -100000;
	
    for(i = 0; i < n; i++)
    {
    	for(j = i; j < n; j++)
    	{
    		temp += array[j];
    		if(i == j)
    		{
    			temp = array[i];
    		}
    		if(max < temp)
    		{
    			max = temp;
    		}
    	}
    }
    return max;
}