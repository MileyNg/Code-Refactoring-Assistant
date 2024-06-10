#include <stdio.h>
main(){
  int a,b,k,ans;
  while(scanf("%d %d",&a,&b)!=EOF){
    ans=0;  
    k=a+b;
    do{    
      k/=10;
      ans++;
    } while(k>0);
    printf("%d\n",ans);
  }
  return 0;
}