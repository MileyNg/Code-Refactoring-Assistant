#include<stdio.h>
main(){
  int i,j,k,l,n,cnt=0;

  while(1){
    if(scanf("%d",&n) == EOF) break;
    cnt=0;
      for(i=0;i<=9;i++){
	for(j=0;j<=9;j++){
	  for(k=0;k<=9;k++){
	    for(l=0;l<=9;l++){
	      if(i+j+k+l==n) cnt++;
	    }
	  }
	}
      }
      printf("%d\n",cnt);
  }
  return 0;
}