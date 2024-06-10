#include<stdio.h>
int main()
{
	char c;
	for(;~scanf("%c",&c);c=!putchar(64<c&&c<91?c+32:94<c&&c<121?c-32:c));
}