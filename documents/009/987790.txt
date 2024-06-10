#include <stdio.h>

void sort(int a[]);
void swap(int *a, int *b);

int main(void)
{
	int n;
	int i, j;
	int a[3];

	scanf("%d", &n);
	for (i = 0; i < n; i++){
		scanf("%d %d %d", &a[0], &a[1], &a[2]);

		sort(a);

		if (a[0] * a[0] == (a[1] * a[1] + a[2] * a[2])){
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}

	return (0);
}

void sort(int a[])
{
	int i, j;

	for (i = 0; i < 2; i++){
		for (j = i + 1; j < 3; j++){
			if (a[i] < a[j]){
				swap(a + i, a + j);
			}
		}
	}
}

void swap(int *a, int *b)
{
	*a ^= *b;
	*b ^= *a;
	*a ^= *b;
}