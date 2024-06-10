#include <stdio.h>
#define N 100
int main (){
  int n,i,j,k,key,a[N];

  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  for(k=0;k<n;k++){
    printf("%2d",a[k]);
  }
  printf("\n");
  for(i=1;i<n;i++){  
    key=a[i];
    j=i-1;
    while(j>=0 && a[j]>key){
      a[j+1]=a[j];
      j--; 
    }
    a[j+1]=key;
    for(k=0;k<n;k++){
      printf("%2d",a[k]);
    }
    printf("\n");   
  }
    return 0;
}