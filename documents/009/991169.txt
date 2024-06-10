#include<stdio.h>
int main(){
  int n,s=0,i,j,max;
  int d[5000];
  while(1){
    scanf("%d",&n);
    if(n==0)break;
    max=0;
    for(i=0;i<n;i++){
      scanf("%d",&d[i]);
    }
    for(i=0;i<n;i++){
      s=0;
      for(j=i;i+j<n;j++){
	s+=d[j];
	if(max<s)max=s;
      }
    }
    printf("%d\n",max);
  }
  return 0;
}