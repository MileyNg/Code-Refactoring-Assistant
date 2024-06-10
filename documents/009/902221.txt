#include<stdio.h>
#include<string.h>
#include<math.h>
int N,M,C,i,j,k,l,F[20001]={0},c,tmp,tmp2;
int main()
{
	for(i=-142,c=0;i<142;i++)
			for(j=-142;j<142;j++)
				if(i*i+j*j<20000)
					F[i*i+j*j]=1;

	scanf("%d",&C);
	for(;C--;)
	{
		scanf("%d%d",&M,&N);
		tmp=(abs(M)<abs(N)?abs(N):abs(M))+1;
		for(i=-tmp,c=0;i<tmp;i++)
		{
			for(j=-tmp;j<tmp;j++)
			{
				tmp2=i*i+j*j;
				if(tmp2>0&&(M*i+N*j)%tmp2==0&&(i*N-j*M)%tmp2==0&&tmp2>0&&(M*M+N*N)%(tmp2)==0&&F[(M*M+N*N)/(tmp2)]==1)
				{
					c++;
				}
			}
		}
		puts(c>8?"C":"P");
	}
	return 0;
}