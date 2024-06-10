#include<iostream>
using namespace std;

int main(){
  
  int n,x[n],i;

  scanf("%d",&n);
  
  for( i = 0 ; i < n ; i++){
    scanf("%d",&x[i]);
  }

  for( i = n ; i > 0; i--){
    printf("%d ",x[i-1]);
  }
  printf("\n");

  return 0 ;

}