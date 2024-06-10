#include <stdio.h>

int main(void) {
	int a,b,c,d,i,n,count;
	
	while(scanf("%d\n", &n)==1) {
		count = 0;
		for(a=0;a<10;a++) {
			for(b=0;b<10;b++) {
				for(c=0;c<10;c++) {
					for(d=0;d<10;d++) {
						if(a+b+c+d==n) {
							count ++;
						}
					}
				}
			}
		}
		printf("%d\n", count);
	}	
	return 0;
}