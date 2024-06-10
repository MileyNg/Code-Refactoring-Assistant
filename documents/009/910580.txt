#include<stdio.h>
int main(){
  int h=0,i,N,t=0,j;
  scanf("%d",&N);
  int hairetu[N];
  for(i=0;i<N;i++){
    scanf("%d",&hairetu[i]);
  }  
  for(i=0;i<N;i++){
      h=0;
    for(j=2;j<hairetu[i];j++){
      if(hairetu[i]%j==0)h++;
    }
    if(h==0)t++;
  }
  printf("%d\n",t);  
  return 0;
}