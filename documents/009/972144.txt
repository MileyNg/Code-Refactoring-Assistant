#include<stdio.h>
main(){

  int a[5000],n,i,j;
  int sum=0,ans=-100000000;

  while(1){
    
    scanf("%d",&n);
    if(n==0){
      break;
    }
    
    for(i=0;i<n;i++){
      scanf("%d",&a[i]);
    }
    
    for(i=0;i<=n;i++){
      
      sum=0;
      
      for(j=i;j<n;j++){
	sum += a[j];
	if(sum>ans){
	  ans=sum;
	}
      }
    }
  
  printf("%d\n",ans);
  ans=0;
  
  }

  return 0;
}