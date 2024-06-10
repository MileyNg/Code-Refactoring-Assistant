#include<stdio.h>
main(){

  int tmp,i,j,tr[20],pri[10]={};

  for(i=0;i<20;i++){
    if(scanf("%d",&tr[i]) == EOF){
      break;
    }
  }
  tmp=i;

  for(i=0;i<tmp;i++){
    if(tr[i]==0){
      for(j=i-1;j>=0;j--){
	if(tr[j]!=0){
	  pri[i]=tr[j];
	  tr[j]=0;
	  break;
	}
      }
    }
  }

  for(i=0;i<10;i++){
    if(pri[i]!=0){
      printf("%d\n",pri[i]);
    }
  }
  return 0;
}