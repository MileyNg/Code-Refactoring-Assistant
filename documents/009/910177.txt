#include <stdio.h>
#define N 200005


int main(void){
  int n,r[N],i,j,c=0,d=0;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&r[i]);
  }
  for(i=0;i<n-1;i++){
    for(j=i+1;j<n;j++){
      c=r[j]-r[i];
      if(i==0){
	d=c;
      }
      else if(d<c){
	d=c;
      }
    }
  }
  printf("%d\n",d);
  return 0;
}