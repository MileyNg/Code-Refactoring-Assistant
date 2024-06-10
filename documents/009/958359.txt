#include <stdio.h>

int main(void)
{
	int a,b,c,i,n;
	int d[1000];
	
	scanf("%d\n", &n);
	
	for (i = 0; i < n; i++){
		scanf("%d %d %d", &a, &b, &c);
		if (a > b && a > c){
			if ((a*a) == (b*b+c*c)){
				d[i] = 1;
			}
			else {
				d[i] = 0;
			}
		}
		if (b > a && b > c){
			if ((b*b) == (a*a+c*c)){
				d[i] = 1;
			}
			else {
				d[i] = 0;
			}
		}
		if (c > b && c > a){
			if ((c*c) == (b*b+a*a)){
				d[i] = 1;
			}
			else {
				d[i] = 0;
			}
		}
	}
	
	for (i = 0; i < n; i++){
		if (d[i] == 1){
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
	
	return(0);
}