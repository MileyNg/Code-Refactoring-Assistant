#include <stdio.h>

#define MAX 5000

int main(void) {
	int n;
	
	while( scanf("%d", &n) != EOF ){
		if(n==0) break;
	
		long nums[MAX];
		int i, j;
		long sum, m;
		
		for(i=0; i<n; i++){
			scanf("%ld", &nums[i]);
		}
		long max=nums[0];
		
		for(i=0; i<n;i++) {
			sum=0;
			for(j=i; j<n; j++) {
				sum+=nums[j];
				if(sum > max) max = sum;
			}
		}	
			
		printf("%ld\n", max);

	}

	return 0;
}