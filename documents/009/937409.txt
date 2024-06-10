#include <stdio.h>

int main(void)
{
	int in[100], out[100];
	int i, j, f;
	
	i = 0;
	j = 0;
	
	
	while (scanf("%d", &in[i]) != EOF){
		if (in[i] == 0){
			out[j] = in[i - 1];
			i--;
			j++;
		}
		else {
			i++;
		}
	}
	
	for (f = 0; f < j; f++){
		printf("%d\n", out[f]);
	}
	
	return (0);
}