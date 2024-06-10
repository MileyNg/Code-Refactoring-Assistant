#include <stdio.h>
#include <math.h>

int main(void) {
	int a,b,c,n;
	scanf("%d",&n);
	while (n--){
		scanf("%d %d %d",&a,&b,&c);
		if ((c*c-a*a-b*b)*(a*a-b*b-c*c)*(b*b-c*c-a*a)==0){
			puts("YES");
		}else{
			puts("NO");
		}
	}
	return 0;
}