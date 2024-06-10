#include <stdio.h>

int main(void) {
	int n, c, i, j;
	int A[100005];
	int max_c = 0;
	int w;
	int count;
	scanf("%d %d\n", &n, &c);
	
	for(i=0;i<n;i++) {
		scanf("%d\n", &A[i]);
		if(max_c < A[i]) max_c = A[i];
	}
	
	for(i=max_c;1;i++) {
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