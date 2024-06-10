#include <stdio.h>

char n[105][205];
int dp[105][205]; 

void nor(int len);

int main(void)
{
	int i, j;
	int len;
	
	i = 0;
	while (fgets(n[i], sizeof(n[i]), stdin) != NULL){
		i++;
	}
	
	len = i;
	nor(len);
	
	for (i = 0; i < len; i++){
		j = 0;
		while (dp[i][j] != -1){
			
			if (i < len / 2){
				if (j == 0){
					dp[i + 1][j] += dp[i][j];
				}
				if (dp[i][j] < dp[i][j + 1] && dp[i + 1][j + 1] != -1){
					dp[i + 1][j + 1] += dp[i][j + 1];
				}
				else if (dp[i + 1][j + 1] != -1){
					dp[i + 1][j + 1] += dp[i][j];
				}
			}
			else{
				if (dp[i][j] < dp[i][j + 1] && dp[i + 1][j] != -1){
					dp[i + 1][j] += dp[i][j + 1];
				}
				else if (dp[i + 1][j] != -1){
					dp[i + 1][j] += dp[i][j];
				}
			}
			j++;
		}
	}
	
	
	
	printf("%d\n", dp[len - 1][0]);
	
	return (0);
}




void nor(int len)
{
		int i, j, k;
		
		for (i = 0; i < len; i++){
			j = k = 0;
			while (n[i][j] != '\n'){
				
				if ('0' <= n[i][j] && n[i][j] <= '9'){
					
					dp[i][k] = n[i][j] - '0';
					if ('0' <= n[i][j + 1] && n[i][j + 1] <= '9'){
						dp[i][k] = dp[i][k] * 10 + n[i][j + 1] - '0';
						j++;
					}
					k++;
				}
				j++;
			}
			dp[i][k] = -1;
		}
		
}