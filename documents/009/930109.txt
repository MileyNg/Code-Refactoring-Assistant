// AOJ0009

#include<stdio.h>

int main(){
	int n, i, j, k, ans;

	while(scanf("%d", &n) != EOF){
		ans = 0;

		for(i = 2; i <= n; i++){
			k = 0;
			for(j = 2; j < i; j++){
				if(i%j == 0)
					k += 1;
			}
			if(k == 0)
				ans += 1;
		}
		printf("%d\n", ans);
	}

	return 0;
}