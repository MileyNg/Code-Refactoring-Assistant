#include <stdio.h>

int main(void)
{
	int a, b, c;
	int n;
	int i;
	
	scanf("%d", &n);
	
	for (i = 0; i < n; i++){
		scanf("%d %d %d", &a, &b, &c);
		a *= a;
		b *= b;
		c *= c;
		
		if (a == b + c || b == a + c || c == a + b){
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
	
	return (0);
}