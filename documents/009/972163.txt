#include<stdio.h>
main(){
  int a,i,j,sum,v[5000],ans;
  while(1){
    scanf("%d",&a);  ans = -100000000;
    if(a==0)break;
    for(i=0;i<a;i++){
      scanf("%d",&v[i]);
    }
    for(i=0;i<a;i++){
      sum=0;
      for(j=i;j<a;j++){
	sum+=v[j];
	if(sum>ans){
	  ans=sum;
	}
      }
    }
    printf("%d\n",ans);
  }
  return 0;
}

    
    