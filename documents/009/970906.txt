#include<stdio.h>

int main(){
  int stp[10];
  int car;
  int i;

  for(i=0;i<10;i++){
    stp[i]=0;
  }

  i=0;
  while(scanf("%d",&car)!=EOF){
    if(car==0){
      printf("%d\n",stp[i-1]);
      stp[i-1]=0;
      i--;
    }
    else{
      stp[i]=car;
      i++;
    }
  }
  return 0;
}