#include <cstdio>

int a[15000];

int main()
{
	int N, min = 99999999, max = -99999999;
	long long int sum = 0;

	scanf(" %d", &N);

	for (int i = 0; i < N; ++i)
	{
		scanf(" %d", &a[i]);
	}

	for (int i = 0; i < N; ++i)
	{
		sum += a[i];
		if (max < a[i]) {
			max = a[i];
		}
		if (min > a[i]) {
			min = a[i];
		}
	}

	printf("%d %d %lld\n", min, max, sum);

	return 0;
}