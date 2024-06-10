#include <stdio.h>

#define N 100000
#define Q 50000

main()
{
  int i, j, count=0;
  int n[N], q[Q];
  
  scanf("%d", &n[0]);
  for(i=1; i<n[0]+1; i++)
    {
      scanf("%d", &n[i]);
    }
  scanf("%d", &q[0]);
  for(i=1; i<q[0]+1; i++)
    {
      scanf("%d", &q[i]);
    }
  
  for(i=1; i<n[0]+1; i++)
    {
      for(j=1; j<q[0]+1; j++)
	{
	  if(n[i] == q[j])
	    {
	      count = count + 1;
	    }
	}
    }
    printf("%d\n", count);
  }