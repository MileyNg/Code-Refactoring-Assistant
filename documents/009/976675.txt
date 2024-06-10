#include<stdlib.h>
#include<stdio.h>

int main(){

  int i,n,x,y,z;

  
  
  scanf("%d",&i);
  
  for(n=0;n<i;++n){

    scanf("%d %d %d",&x,&y,&z);

    x = x*x+y*y;

    z = z*z;


    if(x == z){
      printf("YES");
    }
    else{
      printf("NO");
    }

  }
    return 0;    
}