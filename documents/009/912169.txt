#include<stdio.h>
#include<math.h>

double gcd(double []);//最大公約数
void lcm(double []);//最小公倍数

int main(void)
{
	double number[3];

	while(scanf("%lf %lf",&number[0],&number[1]) != EOF){
	lcm(number);
	}
   return 0;
}


double gcd(double number[])
{
	double i,a;
   
	if(number[0] < number[1]){
		number[2] = number[0];
		number[0] = number[1];
		number[1] = number[2];
   	}
	while(fmod(number[0],number[1])!=0){
		number[0] = fmod(number[0],number[1]);
		number[2] = number[0];//並び替え//
		number[0] = number[1];
		number[1] = number[2];
	}
	printf("%.0f ",number[1]);
	return number[1];
}

void lcm(double number[])
{
	double a;
	a=number[0] * number[1];
	a/=gcd(number);
	printf("%.0f\n", a);
}