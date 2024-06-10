#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int main(void)
{
  int n,*a,i,j,k,tmp,max;
  while(1){
    scanf("%d",&n);
    if(n==0)
      break;
    a=malloc(sizeof(int)*n);
    for(i=0;i<n;i++)
      scanf("%d",&a[i]);

    //for(i=0;i<n;i++)
    // printf("%d\n",a[i]);

    max=-9999;
    tmp=0;
    for(i=0;i<n;i++){
      for(j=1;j<=n-i;j++){
	for(k=i;k<i+j;k++)
	  tmp+=a[k];
	//printf("tmp=%d\n",tmp);
	if(tmp>max)
	  max=tmp;
	tmp=0;
      }
    }
    printf("%d\n",max);
  }

  return 0;
}