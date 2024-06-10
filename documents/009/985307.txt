#include<stdio.h>
#include<string.h>
#include<math.h>

const int INF = 1<<20;
int X,Y,dp[5][1005],ps[5][1005][2],pc[5],S[2],G[2],i,j,fp,rd,rp;char c;
int dis(int a[2],int b[2]){return abs(a[0]-b[0])+abs(a[1]-b[1]);}
int min(int a,int b){return a<b?a:b;}
int main()
{
	for(;scanf("%d%d\n",&X,&Y),X;)
	{
		memset(pc,0,sizeof(pc));
		rd=rp=INF;
		for(i=0;i<Y;i++)
			for(j=0;j<=X;j++)
			{
				c=getchar();
				if(c=='S'){S[0]=i;S[1]=j;}
				else if(c=='G'){G[0]=i;G[1]=j;}
				else if(48<c){c-='1';ps[c][pc[c]][0]=i;ps[c][pc[c]][1]=j;pc[c]++;}
			}
		for(fp=0;fp<5;fp++)
		{
			int np=(fp+1)%5,nnp;
			memset(dp,0x7f,sizeof(dp));
			for(i=0;i<pc[np];i++)dp[np][i]=dis(S,ps[np][i]);//init
			for(nnp=(np+1)%5;nnp!=fp;np=(np+1)%5,nnp=(nnp+1)%5)
				for(i=0;i<pc[np];i++)
					for(j=0;j<pc[nnp];j++)
						dp[nnp][j]=min(dp[nnp][j],dp[np][i]+dis(ps[np][i],ps[nnp][j]));
			for(np=(fp+4)%5,i=0;i<pc[np];i++)
			{
				if(rd>dp[np][i]+dis(ps[np][i],G))
				{
					rd=dp[np][i]+dis(ps[np][i],G);
					rp=fp+1;
				}
			}
		}
		if(rd==INF)puts("NA");
		else printf("%d %d\n",rp,rd);
	}
	return 0;
}