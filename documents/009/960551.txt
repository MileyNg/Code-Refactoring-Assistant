#include<stdio.h>
#include<math.h>

#define FALSE 0
#define TRUE 1

struct point
{
	double x;
	double y;
};

void initialize(double array[], int n);
double calculate_edge(double edge[], double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4);
double helon(double edge1, double edge2, double edge3);
int judge(double area[]);
void output(int flag);
main()
{
	struct point a = {0, 0};
	struct point b = {0, 0};
	struct point c = {0, 0};
	struct point d = {0, 0};
	int flag = 0;
	double edge[6]; //辺の長さを代入する為の配列
	double area[4]; //面積を代入する為の配列
	initialize(edge, 6);
	initialize(area, 4);
	
	while(scanf("%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf", &a.x, &a.y, &b.x, &b.y, &c.x, &c.y, &d.x, &d.y) != EOF)
	{
		calculate_edge(edge, a.x, a.y, b.x, b.y, c.x, c.y, d.x, d.y);
		area[0] = helon(edge[0], edge[1], edge[2]);
		//printf("area[0] = %lf\n", area[0]);
		area[1] = helon(edge[0], edge[3], edge[5]);
		//printf("area[1] = %lf\n", area[1]);
		area[2] = helon(edge[1], edge[3], edge[4]);
		//printf("area[2] = %lf\n", area[2]);
		area[3] = helon(edge[2], edge[4], edge[5]);
		//printf("area[3] = %lf\n", area[3]);
		flag = judge(area);
		output(flag);
		initialize(edge, 6);
	initialize(area, 4);
	}
	return 0;
}

void initialize(double array[], int n)
{
	int i = 0;
	for(i = 0; i < n; i++)
	{
		array[i] = 0;
	}
}

double calculate_edge(double edge[], double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4)
{
	edge[0] = sqrt(pow(x1 - x4, 2) + pow(y1 - y4, 2));
	edge[1] = sqrt(pow(x2 - x4, 2) + pow(y2 - y4, 2));
	edge[2] = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
	edge[3] = sqrt(pow(x3 - x4, 2) + pow(y3 - y4, 2));
	edge[4] = sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2));
	edge[5] = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2));
}

double helon(double edge1, double edge2, double edge3)
{
	double s = (edge1 + edge2 + edge3) / 2;
	double result = sqrt(s * (s - edge1) * (s - edge2) * (s - edge3));
	return result;
}
int judge(double area[])
{
	int i = 0, j = 0, temp = 0;
	for(i = 0; i < 4; i++)
	{
		for(j = i; j < 4; j++)
		{
			if(area[i] < area[j])
			{
				temp = area[i];
				area[i] = area[j];
				area[j] = temp;
			}
		}
	}
	
	if(area[0] <= (area[1] + area[2] + area[3]))
	{
		return TRUE;
	}
	else
	{
		return FALSE;
	}
}
void output(int flag)
{
	if(flag == TRUE)
	{
		puts("YES");
	}
	else
	{
		puts("NO");
	}
}