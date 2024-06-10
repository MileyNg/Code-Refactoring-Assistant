/*
  AOJ 2565
  Title:Broken Audio Signal
  @kankichi573
*/
#include <stdio.h>
#include <limits.h>
#include <ctype.h>
#define max(x,y) (((x)>(y))?(x):(y))
#define min(x,y) (((x)<(y))?(x):(y))
int N,a[1000],x[1000];

void solve()
{
  int i,up,low,none_f;

  up=INT_MAX;
  low=INT_MIN;
  none_f=0;
  for(i=0;i<N-1;i++)
    {
      if(x[i]==-1)  // x
	{
	  if(x[i+1]==-1)
	    {
	      none_f=-1;
	      break;
	    }
	  else
	    {
	      if((i%2)==0)
		up=min(up,a[i+1]);
	      else
		low=max(low,a[i+1]);
	    }
	}
      else        // number
	{
	  if(x[i+1]==-1)
	    {
	      if((i%2)==1)
		up=min(up,a[i]);
	      else
		low=max(low,a[i]);
	    }
	  else
	    {
	      if((i%2)==1)
		{
		if(a[i]<=a[i+1])
		  {
		    none_f=-1;
		    break;
		  }
		}
	      else
		{
		    if(a[i]>=a[i+1])
		      {
			none_f=-1;
			break;
		      }
		}		 
	    }
	}
    }

  //printf("UP=%d low=%d\n",up,low);
   if(low+2>up || none_f)
    {
      printf("none\n");
      return;
    }
   else if(low+2==up)
    {
      printf("%d\n",(low+up)/2);
      return;
    }

 AMB:
    printf("ambiguous\n");

}
dump()
{
  int i;
  
  for(i=0;i<N;i++)
    if(x[i])
      printf("x ");
    else
      printf("%d ",a[i]);
  printf("\n");
}
main()
{
  int i;
  char c;

  while(scanf("%d ",&N) && N)
    {
      for(i=0;i<100;i++)
	a[i]=x[i]=0;

      //      printf("N=%d\n",N);
      for(i=0;i<N;i++)
	{
	LOOP:
	  c=fgetc(stdin);
	  if(!isprint(c) || isspace(c))
	    goto LOOP;
	  else if(c=='x')
	    x[i]=-1;
	  else
	    {
	      x[i]=0;
	      ungetc(c,stdin);
	      scanf("%d ",&a[i]);
	    }
	}
      //dump();
      solve();
    }
  return(0);
}