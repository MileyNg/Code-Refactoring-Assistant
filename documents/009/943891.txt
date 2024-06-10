#include <stdio.h>
#define MAX 100000
int main(){
  int a,b,A[MAX],B[MAX],count=0,i,j;
  scanf("%d",&a);
  for(i=0;i<a;i++){
    scanf("%d",&A[i]);
  }
  scanf("%d",&b);
  for(i=0;i<b;i++){
    scanf("%d",&B[i]);
  }
  
  for(i=0;i<a;i++){
    for(j=0;j<b;j++){
      if(A[i]==B[j]){count++;break;}
    }
  }
  printf("%d\n",count);
  return 0;
}