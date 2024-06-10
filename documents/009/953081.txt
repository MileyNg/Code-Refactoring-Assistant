/*
  AOJ 2576
  Title:Doctor Course Is Recommended
  @kankichi573
*/
#include <stdio.h>

#define max(x,y) (((x)>(y))?(x):(y))
#define min(x,y) (((x)<(y))?(x):(y))
int D,x,y;
int d_point[100];
int dd_point[50];
int d_count,dd_count;
void dump()
{
  int i;
  for(i=0;i<x;i++)
    printf("%d:",d_point[i]);
  printf("\n");
  for(i=0;i<x;i++)
    printf("%d:",dd_point[i]);
  printf("\n");
}
int compare(const void *a, const void *b)
{
    return *(int*)b - *(int*)a;
}
int solve()
{
  int i,j,max_,sum1,sum2,sum;

  if(x>0)
    qsort(d_point,x ,sizeof(int),compare);
  if(y>0)
    qsort(dd_point,y,sizeof(int),compare);

  //dump();
  
  max_=0;
  
  for(i=0;i<=min(y,D/2);i++)
    {
      sum1=sum2=0;
      for(j=0;j<i;j++)
	sum1 += dd_point[j];

      for(j=0;j<min(D-2*i,x);j++)
	sum2 += d_point[j];
      sum=sum1+sum2;
#ifdef DEBUG
      printf("i=%d,s=%d %d %d\n",i,sum1,sum2,sum);
#endif
      if(sum>max_)
	max_=sum;
    }
  
  return(max_);
}

main()
{
  int i,point,ret;
  char ans[3];

  scanf("%d",&D);
  scanf("%d",&x);

  d_count=0;
  for(i=0;i<x;i++)
    {
      scanf("%s %d ",&ans[0],&point);
      if(ans[0]=='D')
	{
	  d_point[d_count]=point;
	  d_count++;
	}
    }
  scanf("%d",&y);
  dd_count=0;
  for(i=0;i<y;i++)
    {
      scanf("%s %d",&ans[0],&point);
      if(ans[0]=='D' && ans[1]=='D')
	{
	  dd_point[dd_count]=point;
	  dd_count++;
	}
    }
  ret=solve();
  printf("%d\n",ret);

  return(0);
}