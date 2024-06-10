#include <stdio.h>

int main(void) {
	int n, c, i, j;
	int A[100005];
	int max_c = 0;
	int w;
	int count;
	int ave;
	scanf("%d %d\n", &n, &c);
	
	ave = 0;
	for(i=0;i<n;i++) {
		scanf("%d\n", &A[i]);
		if(max_c < A[i]) max_c = A[i];
		ave += A[i];
	}
	ave /= c;
	
	for(i=ave;1;i++) {
		w = i;
		count = c - 1;
		for(j=0;j<n;j++) {
			if(w >= A[j]) {
				w -= A[j];
			} else {
				count--;
				w = i;
				w -= A[j];
			}
			
			if(count < 0) {
				break;
			}
		}
		
		if(count == 0) {
			printf("%d\n", i);
			break;
		}
	}
	
	return 0;
}