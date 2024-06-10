// AOJ
#include<stdio.h>

int sum2(int);
int sum3(int);

int sum2(int n){
	if(n >= 0 && n <= 18){
		if(n <= 9)
			return n+1;
		else
			return 19-n;
	}
	else
		return 0;
}


int sum3(int n){
	int i;
	if(n >= 0 && n <= 27){
		int ans = 0;
		for(i=0; i<=9; i++){
			if(i <= n)
				ans += sum2(n-i);
		}
		return ans;
	}
	else
		return 0;
}

int main(){
	int n, i;
	int ans;
	while(scanf("%d", &n) != EOF){
		ans = 0;
		for(i=0; i<=9; i++){
			if(i <= n)
				ans += sum3(n-i);
		}
		printf("%d\n", ans);
	}
	return 0;
}