#include<stdio.h>
main(){
  int z=0;
  int a=0;
  int b=0;
  int c=0;
  int d=0;
  int e=0;
  int f=0;
  int g=0;
  int A[10]={0};
  for(z=0;z<10;z++){
    A[z]=z;
  }
  while(scanf("%d",&a)!=EOF){
    for(b=9;b>=0;b--){
      for(c=9;c>=0;c--){
	for(d=9;d>=0;d--){
	  for(e=9;e>=0;e--){
	    f=b+c+d+e;
	    if(f==a){
	      g=g+1;
	    }
	  }
	}
      }
    }
    printf("%d\n",g);
    f=0;
    g=0;
  }
  return 0;
}