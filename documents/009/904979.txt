#include<stdio.h>
#include<stdlib.h>
int N,M,R[101],K[101][2],i,j,p,t,r;

int c(const void *a,const void *b)
{
	if(((int*)a)[0]==((int*)a)[0])
		return ((int*)a)[1]-((int*)b)[1];
	return ((int*)b)[0]-((int*)a)[0];
}

int main()
{
	scanf("%d%d",&N,&M);
	for(i=0;i<M;i++)
		scanf("%d%d",&K[i][0],&K[i][1]);
	qsort(K,M,sizeof(int[2]),c);
	for(i=r=0,p=1;i<M&&p<=N;)
	{
		for(j=i,t=-1;j<M;j++)
			if(K[j][0]<=p&&(t==-1||K[t][1]<=K[j][1]))
				t=j;
		if(t==-1)break;
		r++;
		p=K[t][1]+1;
		i=t+1;
	}
	if(p<=N)puts("Impossible");
	else printf("%d\n",r);
	return 0;
}