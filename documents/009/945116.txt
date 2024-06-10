#include <stdio.h>
#define N 10000
#define T 500

main()
{

  int i,j;
  int A[N],B[T];
  int n,t,f=0;
  
  scanf("%d",&n);
  
  for(i = 0; i < n; i++){
    scanf("%d",&A[i]);;
  }

  scanf("%d",&t);
  
  for(j = 0; j < t; j++){
    scanf("%d",&B[j]);;
  }
  
  
  for(i = 0; i < n; i++){
    for(j = 0; j < t; j++){
      if(A[i] == B[j]){
	f++;
      }
    }
  }
  
  printf("%d\n",f);

  return 0;
  
}