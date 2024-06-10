/*素数の個数を表示*/
#include<stdio.h>
int hantei (int ,int *,int);
int main()
{
  int n,i,j;
  int A[10000],sosuu[10000];
  int num=3,ans=1,sonum=0; /*ansはフラグ、sonumは最終的な答え*/
  sosuu[0] = 2;
  sosuu[1] = 3;
  sosuu[2] = 5;

  scanf("%d",&n);
  for(i=0;i<n;i++)
    {
      scanf("%d",&A[i]);
    }

  for(i=0;i<n;i++)
    {
      ans = hantei(A[i],sosuu,num);
      if(ans==1) 
	{
	  num++;
	  sonum++;
	}
    }
  printf("%d\n",sonum);
  return 0;
}

int hantei (int a,int *sosuu,int num)
{
  int i;
  for(i=0;i<num;i++)
    {
      if(a==sosuu[i]) return 1;
     else if(a%sosuu[i]==0)
	{
	  return 0;
	}
    }
  sosuu[i] = a;
  return 1;
}