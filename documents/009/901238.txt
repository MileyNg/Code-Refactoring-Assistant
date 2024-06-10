#include<stdio.h>
#define N 1000000
unsigned int TBL[N];
void tbl(){
	unsigned int a,b;
	for(a=1;a<=N;a++) TBL[a]=0;
	for(a=2;a<=N;a++){
		if(TBL[a]==0){
			for(b=2;a*b<=N;b++) TBL[a*b]=1;
		}
	}
}
int main(void){
	int i,n,kosu;
	tbl();
	while(scanf("%d",&n)!=EOF){
		kosu=0;
		for(i=2;i<=n;i++){
			if(TBL[i]==0) kosu++;
		}
		printf("%d\n",kosu);
	}
	return 0;
}