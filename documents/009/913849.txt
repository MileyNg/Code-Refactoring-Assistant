#include<stdio.h>

int maxsum(int *seq, int len);
int seqsum(int *seq, int i, int j);


int main(void){
	int n, i, seq[5000];
	while(1){
		scanf("%d",&n);
		if(n==0) break;
		for(i =0; i<n; i++){
			scanf("%d",&seq[i]);
		}
		printf("%d\n",maxsum(seq,n));
	}
	return 0;
}

int maxsum(int *seq, int len){
	int sum = seq[0], i, j;
	for(i=0; i<len; i++){
		int tmpsum=0;
		for(j=i; j<len; j++){
			tmpsum += seq[j];
			if(tmpsum > sum) sum = tmpsum;
		}
	}
	return sum;
}