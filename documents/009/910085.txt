#include <stdio.h>
int main()
{
  int a, b;
  scanf("%d%d", &a, &b);
  while( a != b )
    {
      if( a > b )
	{
	  a = a- b;
	}
      else if( a < b )
	{
	  b = b - a;
	}
    }
  printf("%d\n", a); 
 return 0;
}