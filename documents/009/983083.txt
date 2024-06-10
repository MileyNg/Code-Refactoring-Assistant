#include <stdio.h>
main(){
  int n,i;
  double ans=100000;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    ans=ans*1.05;
    ans=ans/1000+0.9;
    ans=(int)ans*1000;
  }
  printf("%g\n",ans);
  return 0;
}