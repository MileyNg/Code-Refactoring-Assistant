#include<stdio.h>

void kansu(int,int);

	int data[91][91];
	int n,m;
	int max,cnt;

int main(void)
{
	int i,j;
	int x,y;
	scanf("%d",&m);
	scanf("%d",&n);
	while(m!=0 && n!=0){
		max=0;
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				scanf("%d",&data[i][j]);
			}
		}
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				if(data[i][j]==1){
					cnt=1;
					data[i][j]=0;
					kansu(i,j);
					data[i][j]=1;
				}
			}
		}
		printf("%d\n",max);
		scanf("%d",&m);
		scanf("%d",&n);
	}
	return 0;
}
void kansu(int x,int y)
{
	
	if(x-1>=0){
		if(data[x-1][y]==1){
			cnt++;
			if(cnt>max){
				max=cnt;
			}
			data[x-1][y]=0;
			kansu(x-1,y);
			data[x-1][y]=1;
			cnt--;
		}
	}
	if(x+1<=m){
		if(data[x+1][y]==1){
			cnt++;
			if(cnt>max){
				max=cnt;
			}
			data[x+1][y]=0;
			kansu(x+1,y);
			data[x+1][y]=1;
			cnt--;
		}
	}
	if(y-1>=0){
		if(data[x][y-1]==1){
			cnt++;
			if(cnt>max){
				max=cnt;
			}
			data[x][y-1]=0;
			kansu(x,y-1);
			data[x][y-1]=1;
			cnt--;
		}
	}
	if(y+1<=n){
		if(data[x][y+1]==1){
			cnt++;
			if(cnt>max){
				max=cnt;
			}
			data[x][y+1]=0;
			kansu(x,y+1);
			data[x][y+1]=1;
			cnt--;
		}
	}
}