#include<stdio.h>
main(){
  int n,a,b,c,d,i=0;
  while(scanf("%d",&n)!=EOF){;
    for(a=0;a<=9;a++){
      for(b=0;b<=9;b++){
	for(c=0;c<=9;c++){
	  for(d=0;d<=9;d++){
	    if(a+b+c+d==n){
	      i++;
	    }
	  }
	}
      }
    }
    printf("%d\n",i);
    i=0;
  }
  return 0;
}