#include<stdio.h>
#include<stdbool.h>
#define MIN(a,b) (((a)<(b)) ? (a) : (b))
#define MAX(a,b) (((a)>(b)) ? (a) : (b))

int main()
{
  int n;
  while(scanf("%d",&n)!=EOF)
    {
      int a,b,c,d,count=0;
      for(a=0;a<=9;a++){
	for(b=0;b<=9;b++){
	  for(c=0;c<=9;c++){
	    for(d=0;d<=9;d++){
	      if(a+b+c+d==n) count++;
	    }
	  }
	}
      }
      printf("%d\n",count);
    }
}