#include<stdio.h>
#include<string.h>
#define MAX(x,y) (((x)>(y))?(x):(y))

int count(int x,int y){
	int i,c=0;
	for(i=0;i<16;i++)if(((x>>i)&1)==1 && ((y>>i)&1)==1)c++;
	return c;
}
int dp[32][(1<<16)+1];
int a[33],b[33];
int main(){
	int i,j,n,c,k,f,cb;
	int ans;
	while(1){
		scanf("%d%d",&n,&c);
		if(n==0 && c==0)break;
		
		for(i=0;i<n;i++){
			a[i]=0;
			for(j=0;j<16;j++){
				scanf("%d",&f);
				a[i]|=(1<<j)*f;
			}
		}
		for(i=0;i<c;i++){
			b[i]=0;
			for(j=0;j<16;j++){
				scanf("%d",&f);
				b[i]|=(1<<j)*f;
			}
		}

		b[c]=0;c++;
		for(i=0;i<n+1;i++)for(j=0;j<(1<<16);j++)dp[i][j]=-1;
		
		dp[0][0]=0;
		for(i=0;i<n;i++){
			for(j=0;j<(1<<16);j++){
				if(dp[i][j]<0)continue;
				cb=j|a[i];
				for(k=0;k<c;k++){
                    dp[i+1][cb&(~b[k])]
						=MAX(dp[i+1][cb&(~b[k])],dp[i][j]+count(cb,b[k]));
				}
			}
		}

		ans=0;
		for(j=0;j<(1<<16);j++)ans=MAX(ans,dp[n][j]);
		printf("%d\n",ans);

	}
	return 0;
}