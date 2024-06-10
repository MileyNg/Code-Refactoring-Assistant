#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int main(void)
{
  int queue=0,a[10],n;  

  while(scanf("%d",&n)!=EOF){
    if(n==0){
      printf("%d\n",a[queue-1]);
      queue--;
    }
    else{
      a[queue++]=n;
    }
  }
  return 0;
}