#include <stdio.h>
#include <math.h>
main(){
  int a,c1,c2=0,i,j,n[10000];
  scanf("%d",&a);
  for(i = 0; i < a; i++){
    scanf("%d",&n[i]);
  }
  for(i = 0; i < a; i++){
    c1 = 0;
    for(j = 2; j <= sqrt(n[i]); j++){
      if(n[i]%j == 0) c1++;
    }
    if(c1 == 0) c2++;
  }
  printf("%d\n",c2);
  return 0;
}