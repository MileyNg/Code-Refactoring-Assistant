#include<stdio.h>
int main(){
  int ire[10]={0};
  int n;
  int i=0;

  while(scanf("%d",&n)!=EOF){
    if(n==0){
      i--;
      printf("%d\n",ire[i]);
    }
    else{
      ire[i]=n;
      i++;
    }
  }
}