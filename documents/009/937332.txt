#include<stdio.h>
main(){
  int a,b,c,d,A[100];
  scanf("%d",&a);
  for(b=0;b<a;b++){
    scanf("%d",&A[b]);
  }
  for(b=0;b<a;b++){
    for(c=a-1;c>b;c--){
      d=A[c];
      A[c]=A[c-1];
      A[c-1]=d;
    }
  }
  for(b=0;b<a;b++){
    if(b==a-1){
      printf("%d\n",A[b]);
    }
    else{
      printf("%d ",A[b]);
    }
  }
  return 0;
}