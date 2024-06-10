#include <stdio.h>

void reverse()
{
	char c = getchar();
	if (c != '\n')
	{
		reverse();
		putchar(c);
	}
}

int main() {
	reverse();
	return 0;
}