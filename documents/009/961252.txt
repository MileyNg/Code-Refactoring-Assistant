#include <stdio.h>
#include <math.h>

int main(void) {

	int n=0, i, j;
	int a[80000];
	
	a[0] = 2;
	a[1] = 3;
	
	while( scanf("%d", &n) != EOF ) {
		int count = 2;
		
		if(n==1 || n==2 || n==3) {
			printf("%d\n", n-1);
			continue;
		}
		
		else {
			for(j=5; j<=n; j=j+2){
				for(i=0; i<count; i++) {
					if(j%a[i]== 0) break;
				
					if(i == count -1){
						a[count++] = j;
					}
				}
			}
			printf("%d\n", count);
			
		}
	
	}
	
	return 0;
}