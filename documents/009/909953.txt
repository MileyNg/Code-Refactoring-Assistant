#include <stdio.h>
#include <math.h>


int main(void){
  int a[10005],count=0,i,j,f,n;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  for(i=0;i<n;i++){
    f=1;
    for(j=2;j<=sqrt(a[i]);j++){
      if(a[i]%j==0){
	f=0;
      }
    }
    if(a[i]==1)continue;
    if(f==1){
      count++;
    }
  }
  printf("%d\n",count);
  
  return 0;
}