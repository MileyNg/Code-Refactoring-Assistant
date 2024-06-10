#include <stdio.h>

typedef struct {
	int s,t,c;
} edge_t;

int getId(int town,int ticket) {
	return ticket*100+town;
}

int main(void) {
	static int edgeNum;
	static int cost[11*100];
	static edge_t edges[500*11*2*2];
	int c,n,m,s,d;
	while(scanf("%d%d%d%d%d",&c,&n,&m,&s,&d)==5 && (c|n|m|s|d)!=0) {
		int i,j;
		int answer;
		edgeNum=0;
		for(i=0;i<m;i++) {
			int a,b,f;
			scanf("%d%d%d",&a,&b,&f);
			a--;b--;
			for(j=1;j<=c;j++) {
				edges[edgeNum].s=getId(a,j);
				edges[edgeNum].t=getId(b,j);
				edges[edgeNum].c=f;
				edgeNum++;
				edges[edgeNum].s=getId(a,j);
				edges[edgeNum].t=getId(b,j-1);
				edges[edgeNum].c=f/2;
				edgeNum++;
				edges[edgeNum].s=getId(b,j);
				edges[edgeNum].t=getId(a,j);
				edges[edgeNum].c=f;
				edgeNum++;
				edges[edgeNum].s=getId(b,j);
				edges[edgeNum].t=getId(a,j-1);
				edges[edgeNum].c=f/2;
				edgeNum++;
			}
			edges[edgeNum].s=getId(a,0);
			edges[edgeNum].t=getId(b,0);
			edges[edgeNum].c=f;
			edgeNum++;
			edges[edgeNum].s=getId(b,0);
			edges[edgeNum].t=getId(a,0);
			edges[edgeNum].c=f;
			edgeNum++;
		}
		for(i=0;i<11*100;i++)cost[i]=100000000;
		cost[getId(s-1,c)]=0;
		for(i=0;i<11*100;i++) {
			for(j=0;j<edgeNum;j++) {
				if(cost[edges[j].t]>cost[edges[j].s]+edges[j].c) {
					cost[edges[j].t]=cost[edges[j].s]+edges[j].c;
				}
			}
		}
		answer=100000000;
		for(i=0;i<=c;i++) {
			if(cost[getId(d-1,i)]<answer)answer=cost[getId(d-1,i)];
		}
		printf("%d\n",answer);
	}
	return 0;
}