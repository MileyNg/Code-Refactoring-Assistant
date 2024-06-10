#include<stdio.h>
int main()
{
	int N,a,b,c;
	scanf("%d",&N);
	while(N--){
		scanf("%d %d %d",&a,&b,&c);
		if(a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a)puts("YES");
		else puts("NO");
	}
	return 0;
}