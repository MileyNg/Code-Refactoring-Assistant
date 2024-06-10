#include<stdio.h>
#include<math.h>
#include<string.h>
int main(void)
{
  int n;

  for(;scanf("%d",&n)!=EOF;){
    int a,b,c;
    int count=0;
    for(a=0;a<10;a++){
      for(b=0;b<10;b++){
	for(c=0;c<10;c++){
	  if((n-a-b-c)>=0 && (n-a-b-c)<10)
	    count+=1;
	}
      }
    }
    printf("%d\n",count);
  }

  return 0;
}