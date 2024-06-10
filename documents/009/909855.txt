#include <stdio.h>

int main(){
  int n,m,a;
  scanf("%d%d",&n,&m);
  if(1<n<m){
    while((m%n)!=0){
      a=m%n;
      m=n;
      n=a;
    }
    printf("%d\n",n);
  }
  else if(1<m<n){
    while((n%m)!=0){
      a=n%m;
      n=m;
      m=a;
    }
    printf("%d\n",m);
  }
  return 0;
}