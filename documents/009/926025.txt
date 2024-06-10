#include <stdio.h>

char s[200001];
int array[5000];

int main(void)
{
	int n;
	int i;
	
	scanf("%d", &n);
	while (n != 0){
		for (i = 0; i < n; i++){
			scanf("%d", &array[i]);
		}
		for (i = 0; i < n; i++){
			int j;
			int sum = 0;
			for (j = i; j < n; j++){
				sum += array[j];
				s[sum + 10000]++;
			}
		}
		for (i = 200001; i >= 0; i--){
			if (s[i] > 0){
				printf("%d\n", i - 10000);
				break;
			}
		}
		for (; i >= 0; i--){
			s[i] = 0;
		}
		scanf("%d", &n);
	}
	
	return 0;
}