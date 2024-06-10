#include <stdio.h>

int main(void)
{

  int i,j,k;
  int n,x;
  int count = 0;
  

  while(1){
    scanf("%d %d",&n,&x);
    if(n == 0 && x == 0){
      break;
    }
  
    else {
      for(i = 1;i <= n;i++){
	for(j = i+1;j <= n;j++){
	  for(k = j+1;k <= n;k++){
	    if(i+j+k == x){
	      count++;
	    }
	  }
	}
      }
    }

    printf("%d\n",count);
  }
  return 0;
}
	    
	    
  