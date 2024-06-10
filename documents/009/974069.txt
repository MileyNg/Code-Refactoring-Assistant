#include<stdio.h>
main(){
  int b,c,d,e,n,ans=0;
  while(scanf("%d",&n)!=EOF){
    for(b=0;b<10;b++){
      for(c=0;c<10;c++){
	for(d=0;d<10;d++){
	  for(e=0;e<10;e++){
	    if(b+c+d+e==n){
	      ans=ans+1;
	    }
	  }
	}
      }
    }
    printf("%d\n",ans);
    ans=0;
  }
  return 0;
}