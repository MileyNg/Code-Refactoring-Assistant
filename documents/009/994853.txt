#include <cstdio>

int main(int argc, char const *argv[])
{
	int n;

	scanf(" %d", &n);

	for (int i = 1; i <= n; ++i){
		int x = i;

		if (x % 3 == 0){
			printf(" %d", i);
		}
		else if (x % 10 == 3){
			printf(" %d", i);
		}
		else {
			x /= 10;
			if(x) {
				if (x % 10 == 3){
					printf(" %d", i);
				}
			}
		}
	}
	printf("\n");

	return 0;
}