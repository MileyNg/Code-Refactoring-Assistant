#include <stdio.h>
#include <stdlib.h>

// 最大公約数
int gcd(int m, int n)
{
	// 引数に０がある場合は０を返す
	if ((0 == m) || (0 == n))
		return 0;
	
	// ユークリッドの方法
	while(m != n)
	{
		if (m > n) m = m - n;
		else       n = n - m;
	}
	return m;
}//gcd

// 最小公倍数
int lcm(int m, int n)
{
	// 引数に０がある場合は０を返す
	if ((0 == m) || (0 == n))
		return 0;
	
	return ((m / gcd(m, n)) * n); // lcm = m * n / gcd(m,n)
}//lcm


int main(){

    int a, b;
   
    while(scanf("%d %d", &a, &b) != -1) {
        if(200000000 < a || 200000000 < b){
            exit(0);
        }
        printf("%d %d\n", gcd(a, b), lcm(a, b));
    }
    return 0;
}