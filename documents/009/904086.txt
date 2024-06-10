#include <stdio.h>

int main(void)
{
	int triangle[1000][3];
	int temp;
	int n;
	int i, j, k;

	scanf("%d", &n);
	for(i = 0; i < n; i++){
		scanf("%d %d %d", &triangle[i][0], &triangle[i][1], &triangle[i][2]);
	}

	for(k = 0; k < n; k++){
		for(i = 0; i < 2; i++){
			for(j = 0; j < 2; j++){
				if(triangle[k][j] < triangle[k][j+1]){
					temp = triangle[k][j];
					triangle[k][j] = triangle[k][j+1];
					triangle[k][j+1] = temp;
				}
			}
		}
	}

	for(i = 0; i < n; i++){
		if(triangle[i][0] * triangle[i][0] == triangle[i][1] * triangle[i][1] + triangle[i][2] * triangle[i][2]){
			printf("YES\n");
		}else{
			printf("NO\n");
		}
	}

	return 0;
}