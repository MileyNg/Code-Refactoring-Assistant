#include <stdio.h>
int gcd(int n, int m){
	return (m==0) ? n:gcd(m,n%m);
}

int main(void) {
	int a,b,g,l;
	while (scanf("%d %d",&a,&b)!=EOF){
		g=gcd(a,b);
		printf("%d %d\n",g,a/g*b);
	}
	return 0;
}