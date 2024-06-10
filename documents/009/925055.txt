#include<stdio.h>
#include<math.h>
#define compile 0

double func_rad(int c)
{
	double r = 0;
	r = (c * M_PI) / 180;
	
	return r;
}

double func_edge_length(int a, int b, double c)
{
	double fd = 0;
	fd = sqrt(pow(a, 2) + pow(b, 2) - (2 * a * b) * cos(c));
	
	return fd;
}

double func_edge_sum(int a, int b, double x)
{
	double L = 0;
	L = a + b + x;
	
	return L;
}
double func_cal_height(int b, double c)
{
	double h = 0; 
	h = b * sin(c);
	//printf("");
	return h;
}
double func_cal_S(int a, double h)
{
	double S = 0;
	S = (a * h) / 2;
	
	return S;
}
main()
{
	int a = 0, b = 0, c = 0; //aは底辺、bは与えられる辺、cは2辺の間の角
	double x = 0, cr = 0; //xは与えられていない辺、crはcをラジアンに変換した値
	double S = 0, L = 0, h = 0; //Sは面積、Lは周の長さ、hは高さ
	
	scanf("%d %d %d", &a, &b, &c);
	
	cr = func_rad(c); //cをラジアンに変換
	
	//printf("cのラジアン変換cr = %f\n", cr);
	
	x = func_edge_length(a, b, cr);
	//printf("x = %f\n", x);
	L = func_edge_sum(a, b, x);
	h = func_cal_height(b, cr);
	S = func_cal_S(a, h);
	
	#if compile == 1
	printf("底辺a = %d\n", a);
	printf("辺２b = %d\n", b);
	printf("角度c = %d\n", c);
	printf("cのラジアン変換cr = %f\n", cr);
	printf("辺３x = %f\n", x);
	#endif
	//S,L,h
	printf("%f\n", S);
	printf("%f\n", L);
	printf("%f\n", h);
	
	return 0;
}