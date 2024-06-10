#include <stdio.h>

int main (){
 int i;
 int n;

  scanf("%d" , &n);
  int a[n];
  for ( i = 0; i < n; i++){
    scanf("%d",&a[i]);
  }
  
  for (i = 0; i < n ; i++){
    if(i) {
      printf(" ");
    }
    printf("%d", a[n-i-1]);
  }
  printf("\n");
  return 0;
}