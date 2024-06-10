#include<stdio.h>
main(){
  int n,i,j;
  double x[4],y[4];
  scanf("%d",&n);
  for(i=0;i<n;i++){
    for(j=0;j<4;j++){
      scanf("%lf %lf",&x[j],&y[j]);
	    }
  if((y[1]-y[0])-(x[1]-x[0]) == (y[3]-y[2])-(x[3]-x[2])){
	  printf("YES\n");
	}
	else{
	  printf("NO\n");
	}
  }
    return 0;
    }