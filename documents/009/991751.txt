/*
  AOJ 1056
  Title:Ben Toh
  @kankichi573
*/
#include <stdio.h>
#include <float.h>

double memo[100000][21];
double visit[100000][21];
double solve(int n,int success_days)
{
  double cont_succ,ret;

  //printf("arg=%d %d\n",n,success_days);

  if(n<=0)
    return(0);
  if(success_days<=20 && visit[n][success_days])
    return(memo[n][success_days]);
 
  if(success_days < 20)
    cont_succ=1.0/(double)(1<<success_days);
  else
    cont_succ=0.0;

  if(success_days < 20)
    {
      ret =  cont_succ*(1+solve(n-1,success_days+1));
      ret += (1-cont_succ)*(solve(n-1,0));
    }
  else
    ret = (solve(n-1,0));
  if(success_days==0 && success_days<=20)
    {
    memo[n][success_days]=ret;
    visit[n][success_days]=ret;
    }
  return(ret);
}
main()
{
  int n;
  while(scanf("%d",&n) && n)
    {
      printf("%lf\n",solve(n,0));
    }
  return(0);
}