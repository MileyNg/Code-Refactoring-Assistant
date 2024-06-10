#include<stdio.h>
#include<string.h>
int N,M,G[100],i,j,k,L[100],S,E,R;
int dp[1<<18];
int main()
{
	for(;scanf("%d",&N),N;)
	{
		memset(G,0,sizeof(G));
		for(i=0;i<N;i++)
		{
			
			scanf("%d%d",&M,&L[i]);
			for(j=0;j<M;j++)
			{
				scanf("%d%d",&S,&E);
				S-=6;E-=6;
				G[i]|=((1<<E)-1)-((1<<S)-1);
			}
		}
		memset(dp,-1,sizeof(dp));
		dp[0]=R=0;
		for(i=0;i<(1<<18);i++)
		{
			if(dp[i]==-1)continue;
			for(j=0;j<N;j++)
				if((i&G[j])==0&&dp[i|G[j]]<dp[i]+L[j])
				{
					dp[i|G[j]]=dp[i]+L[j];
					R=R<dp[i]+L[j]?dp[i]+L[j]:R;
				}
		}
		printf("%d\n",R);
	}
	return 0;
}