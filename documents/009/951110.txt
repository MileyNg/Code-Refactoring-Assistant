#include <stdio.h>

int x[5005];

int solve(int l, int u) {
	int m, i, sum, lmax, rmax;
	int r2max, l2max;
	if(l>u) return 0;
	
	if(l==u) {
		return x[l];
	}
	
	m = (l + u) / 2;
	// 左側
	lmax = -200000000;
	sum = 0;
	for(i=m;i>=l;i--) {
		sum += x[i];
		if(lmax < sum) lmax = sum;
	}
	
	// 右側
	rmax = -2000000000;
	sum = 0;
	for(i=m+1;i<=u;i++) {
		sum += x[i];
		if(rmax < sum) rmax = sum;
	}
	
	// さらに分轄
	l2max = solve(l, m);
	r2max = solve(m+1, u);
	if(l2max < r2max) l2max = r2max;
	if(lmax+rmax > l2max) l2max = lmax+rmax;
	return l2max;
}

int main(void) {
	int i, n;
	
	while(scanf("%d\n", &n) == 1) {
		if(n==0) break;
		for(i=0;i<n;i++) {
			scanf("%d\n", &x[i]);
		}
		printf("%d\n", solve(0, n-1));
	}
	
	return 0;
}