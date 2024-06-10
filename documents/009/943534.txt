#include<stdio.h>
#define m(a,b)(a<b?a:b)
#define INF 999999999
int A,B,D,i,j;

int main()
{
	
	for(;scanf("%d%d%d",&A,&B,&D),A+B+D;)
	{
		int b1=INF,b2=INF,b3=INF,Ra=INF,Rb=INF,x;
		for(i=0;i<10000;i++)
		{
			b1=(i*A+D)%B==0?m((i*A+D)/B,b1):b1;
			b2=i*A-D>=0&&(i*A-D)%B==0?m((i*A-D)/B,b2):b2;
			b3=D-i*A>=0&&(D-A*i)%B==0?m((D-A*i)/B,b3):b3;
			x=m(b1,m(b2,b3));
			if(Ra+Rb>x+i||(Ra+Rb==x+i&&Ra*A+Rb*B>i*A+x*B))
			{
				Ra=i;
				Rb=x;
			}
		}
		printf("%d %d\n",Ra,Rb);
	}
	return 0;
}