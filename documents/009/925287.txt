#include<stdio.h>
#include<math.h>

#define compile 0

void func_initial(int fs[], int n)
{
	int i = 0;
	
	for(i = 0; i < n; i++)
	{
		fs[i] = 0;
		#if compile == 1
		printf("fs[%d] = %d\n", i, fs[i]);
		#endif
	}
}

double func_stddev(int fs[], double ave, int num)
{
	double dev = 0, f_sum = 0, x = 0; //xは代入用の変数
	int i = 0;
	
	for(i = 0; i < num; i++)
	{
		x = fs[i] - ave;
		f_sum += pow(x, 2);
		#if compile == 1
		printf("x = %f\n", x);
		printf("f_sum = %f\n", f_sum);
		#endif
	}
	
	dev = (double)f_sum / num;
	
	return dev;
}
main()
{
	int i = 0, n = 0, sum = 0; //iは制御変数、nは人数、sumは合計点
	double a = 0, m = 0; //aは分散、mは平均点 標準偏差はsqrt関数で表示
	
	scanf("%d", &n);
	
	while(n != 0)
	{
		
		int s[n];
		func_initial(s, n); //関数の初期化
		
		for(i = 0; i < n; i++)
		{
			scanf("%d", &s[i]);
			sum += s[i];
			
			#if compile == 1
			printf("s[%d] = %d\n", i, s[i]);
			printf("sum = %d\n", sum);
			#endif
			
		}
		
		m = (double)sum / n;
		
		#if compile == 1
		printf("sum = %d\n", sum);
		printf("m = %f\n", m);
		#endif
		
		a = func_stddev(s, m, n);
		
		printf("%f\n", sqrt(a));
		sum = 0;
		scanf("%d", &n);
	}
	return 0;
}