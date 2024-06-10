#include<stdio.h>
int main(){
  int ri;
  int sya;
  int total,ans;
  scanf("%d",&ri);
  sya = 100000*0.05;
  total = (ri+1)*sya;
  ans = 100000 + total;
  printf("%d\n",ans);
  return 0;
}
    