#include <stdio.h>
 
 int main(){

  int val;
  int i,j,N;
  int count = 0;

  scanf("%d",&val);

	for(i = 0 ;i < val;i++){
	scanf("%d",&N);
	 for(j = 2;j * j <= N;j++){
		 if(N % j == 0)break;
	  }
      if(j * j > N)
		  count++;
	 }
	 printf("%d\n",count);
	 return 0;
 }