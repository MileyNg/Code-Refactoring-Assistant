/*
AOJ 2407
Computer Onesan
2014/6/9 WA 48/74
*/
#include <stdio.h>
#define WARI 1000000 
int M,N; //global
int memo[101][2][2][2];
//last=last movement (0,1,2,-1,-2)
unsigned int power(n,x)
{
  if(x==0)
    return(1);
  else
    return(n*power(n,x-1) % WARI);
}
// never go left pattern
unsigned int f(int y0,int x0,int y1,int x1)
{
  return(power(3,x1-x0));
}
// go left center line x1=>x2
// S->v    --->
// v<--    ^<--
// --->    S->^
int g(int y0,int x0,int y1,int x1)
{
  if(x1>x0 && y1==2 && y0==0)
    return(1);
  if(x1>x0 && y1==0 && y0==2)
    return(1);
  return(0);
}
unsigned long long solve_3(int y0,int x0,int y1,int x1,int last)
{
  // last means last movement if 1  ---V
  //                                V---
  // (called gyaku-S)               --->
  unsigned long long ret;
  int i;
  unsigned long long wk,wk2;

  if(x1==x0)  //updown only
    {
      if(last)
	return(1);
      else
	return(0);
    }
  
  if(x1-x0==1)
    {
      if(last==0 && ((y0==0 && y1==2)||(y1==0 && y0==2))) 
	return(1);
      else if(last==1)
	return(3);
      else
	return(0);
    }
  if(ret=memo[x1-x0][y0/2][y1/2][last])  
    return(ret);


  ret=0;
  if(last)
    {
      for(i=x0;i<=x1;i++)
       {
	 if(i<x1)
	   {
	     wk2 = f(y0,x0,0,i)*solve_3(0,i+1,y1,x1,0);
	     wk2 %= WARI;
	     ret += wk2;
	     ret %= WARI;
	     wk2 = f(y0,x0,2,i)*solve_3(2,i+1,y1,x1,0);
	     wk2 %= WARI;
	     ret += wk2;
	   }
	 else
	   ret += f(y0,x0,0,i);
	 ret %= WARI;
       }
    }
  else 
    {
      for(i=x0+1;i<=x1;i++)
	{
	  if(y0==0)
	    {
	      if(i<x1)
		{
		  wk2 = solve_3(2,i+1,y1,x1,1)+solve_3(2,i+1,y1,x1,0);
		  wk2 %= WARI;
		  wk = g(y0,x0,2,i)*wk2;
		  wk %= WARI;
		  ret  += wk;
		}
	      else
		ret +=1;
	    }
	  else if(y0==2)
	    {
	      if(i<x1)
		{
		  wk2 = solve_3(0,i+1,y1,x1,1)+solve_3(0,i+1,y1,x1,0);
		  wk2 %= WARI;
		  wk  = g(y0,x0,0,i)*wk2;
		  wk %= WARI;
		  ret  += wk;
		}
	    }
	  ret %= WARI;
	}
     }

  memo[x1-x0][y0/2][y1/2][last]=ret;  
  return(ret);
}
s3(int N)
{
  return((solve_3(0,0,2,N,1)
	  +solve_3(0,0,2,N,0)) % WARI
	 );
}

int s2(int N)
{
  return(power(2,N));
}
int solve23(int N,int M)
{
  if(M==2)
    return(s2(N));
  if(M==3)
    return(s3(N));
}
main()
{
  int ret;

#ifdef DEBG
  int i,j;
  for(i=2;i<=100;i++)
    for(j=2;j<=3;j++)
      {
	ret=solve23(i,j);
	printf("%d %d %d\n",i,j,ret);
      }
#else
  scanf("%d %d",&N,&M);
  ret=solve23(N,M+1);
  printf("%d\n",ret);
#endif
  return(0);
}