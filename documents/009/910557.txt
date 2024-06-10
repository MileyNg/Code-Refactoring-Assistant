/*
  AOJ 2523
  Title:Time Complexity
  @kankichi573
  14/04/10 WA 2/26
*/
#include <stdio.h>
#include <string.h>
#include <float.h>
#include <setjmp.h>
jmp_buf jb;

int n,T;
char expr[50];

double expt(int x,int n)
{
  double ret;

  if(n==0)
    ret=1.0;
  else
    ret=x*expt(x,n-1);
  if(ret>1000000000)
    longjmp(jb,1);
  return(ret);
}

double eval_single(char expr[],int n)
{
  int ret;
  if(expr[1]=='^')
    {
      ret=expt(n,expr[2]-'0');
    }
  else
    ret=n;

  return(ret);
}
double evaluate(char exp[],int n)
{
  double ret;
  char *p;

  ret=0;
  p=strtok(exp,"+\0");
    do
    {
      ret+=eval_single(p,n);
      if(ret>1000000000)
	longjmp(jb,1);
    }while(p=strtok(NULL,"+\0"));
  return(ret);
}

main()
{
  double ret;

  scanf("%d %d",&n,&T);
  scanf("%s",expr);

  if(setjmp( jb ) == 0 ) 
    ret=T*evaluate(expr,n);  
  else
    {
      printf("TLE\n");
      return(0);
    }
  if(ret>1000000000)
    printf("TLE\n");
  else
    printf("%.0lf\n",ret);
    
  return(0);
}