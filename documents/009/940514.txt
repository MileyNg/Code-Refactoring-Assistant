#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int N,p[45],t[45],i,j,R,dp[45][4];
int dfs(int n,int c)
{
	int tmp=-9999,TL=t[n+1]-t[n],res=-9999;
	if(dp[n][c]!=-9999)return dp[n][c];
	if(n==N)return dp[n][c]=p[n];
	if(c<3&&abs(p[n]-p[n+1])*(c+1)<=TL)
	{
		tmp=dfs(n+1,p[n+1]==0?0:c+1);
		if(tmp>=0)tmp+=abs(p[n]-p[n+1]);
		res=tmp;
	}
	tmp=-9999;
	if(c>0&&p[n]*(c+1)+p[n+1]<=TL)
	{
		tmp=dfs(n+1,1);
		if(tmp>=0)tmp+=p[n]+p[n+1];
		if(res==-9999&&tmp!=-9999)res=tmp;
		else if(res<0&&tmp>=0)res=tmp;
		else if(res>=0&&tmp<0)res=res;
		else res=res<tmp?res:tmp;
	}
	if(res==-9999)return -(n+1);
	return dp[n][c]=res;
}

int main()
{
	for(;scanf("%d",&N),N;)
	{
		for(i=0;i<45;i++)
			for(j=0;j<4;j++)
				dp[i][j]=-9999;
		for(i=1;i<=N;i++)
			scanf("%d%d",&p[i],&t[i]);
		R=dfs(0,0);
		printf("%s %d\n",R>=0?"OK":"NG",abs(R));
	}
	return 0;
}