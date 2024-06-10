#include<stdio.h>

int main(){
  int a,b,ans=0,i;
  scanf("%d %d",&a,&b);
  if(a>b){
    for(i=1;i<=b;i++){
      if((a%i==0) && (b%i==0)){
	ans = i;
      }
    }
  } else {
    for(i=1;i<=b;i++){
      if((a%i==0) && (b%i==0)){
	ans = i;
      }
    }
  }
  printf("%d\n",ans);
  return 0;
}