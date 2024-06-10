#include <stdio.h>

main()
{
  int a[10000];
  int i, j, length, count = 0, flag = 0;

  scanf("%d", &length);

  for(i = 0; i < length; i++)
    {
      scanf("%d", &a[i]);
    }

  for(i = 0; i < length; i++)
    {
      for(j = 2; j < a[i]; j++)
	{
	  if(a[i] % j == 0)
	    {
	      flag = 1;
	      break;
	    }
	}

      if(flag == 0)
	{
	  count++;
	}
      flag = 0;
    }
  printf("%d\n", count);
  return 0;
}