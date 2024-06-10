#include <stdio.h>
  
int main(){
	int a,b,ans,i;
	while(scanf("%d %d", &a, &b) != EOF){
		ans = a + b;
		for(i = 0; ans != 0; i++){
			ans = ans / 10;
		}
		printf("%d\n", i);
	}
return 0;
}