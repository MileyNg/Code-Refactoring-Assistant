#include<stdio.h>
int main(){
  int ri,i;
  int sya=100000;
  int total,ans;
  scanf("%d",&ri);
  for(i=0;i<ri;i++){
    sya = sya * 1.05;
    if(sya%1000!=0){
      sya = sya-sya%1000+1000;
    }
  }
  printf("%d\n",sya);
  return 0;
}
    