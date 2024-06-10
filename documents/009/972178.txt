#include<stdio.h>
main(){
  int i,j,sum,n,ans;
  int a[5000];
  while(1){
    scanf("%d",&n); ans= -100000000;
    if(n == 0)break;
    for(i=0;i<n;i++){
      scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++){
      sum=0;
      for(j=i;j<n;j++){
	sum += a[j];
	if(sum>ans){
	  ans = sum;
	}
      }
    }
    printf("%d\n",ans);
  }
  return 0;
}