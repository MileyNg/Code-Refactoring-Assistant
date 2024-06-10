#include <stdio.h>

int main(void)
{
	int a, b, c, i, n;
	int sub1, sub2, max;
	
	scanf("%d", &n);
	
	for (i = 0; i < n; i++){
		scanf("%d %d %d", &a, &b, &c);
		if (a >= b && a >= c){
			max = a * a;
			sub1 = b * b;
			sub2 = c * c;
		}
		else if (b > a && b > c){
			max = b * b;
			sub1 = a * a;
			sub2 = c * c;
		}
		else if (c > a && c > b){
			max = c * c;
			sub1 = b * b;
			sub2 = a * a;
		}
		
		if (sub1 + sub2 == max){
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
	
	return (0);
}