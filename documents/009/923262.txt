#include <stdio.h>

int main(void)
{
	int a, b, c, d, e, f;
	int z[3];
	
	scanf("%d", &a);
	
	for (b = 0; b < a; b++) {
		scanf("%d %d %d", &z[0], &z[1], &z[2]);
		for (e = 0; e < 3; e++) {
			for (f = 0; f < 3; f++) {
				if (z[e] < z[f]) {
					c = z[f];
					z[f] = z[e];
					z[e] = c;
				}
			}
		}
		z[0] = z[0] * z[0];
		z[1] = z[1] * z[1];
		z[2] = z[2] * z[2];
		
		if ((z[0] + z[1]) == z[2]) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
	return (0);
}