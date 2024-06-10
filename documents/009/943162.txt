#include <stdio.h>

int main(void){
	
	int a[3];		
	int i, tmp;
	scanf("%d %d %d", &a[0], &a[1], &a[2]);
	
	if(a[0] > a[2]){
		tmp = a[0];
		a[0] = a[2];
		a[2] = tmp;
	}
	
	for(i = 0; i < 2; i++){
		if(a[i] > a[i + 1]){
			tmp = a[i + 1];
			a[i + 1] = a[i];
			a[i] = tmp;
		}
	}	
		
	printf("%d %d %d\n", a[0], a[1], a[2]);
	
	return 0;
}