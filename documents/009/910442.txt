#include <stdio.h>
int isPrime(int);

main(){
  int len,i;
  int A[10000];
  int ans;
  int count=0;


  scanf("%d",&len);

  for(i=0;i<len;i++){
    scanf("%d",&A[i]);
  }

 for(i=0;i<len;i++){
   ans=isPrime(A[i]);
   if(ans == 1){
     count+=1;
   }
 }
  
 printf("%d\n",count);
 return 0;
}



int isPrime( int x ){
  int i;
  if (x <= 1) return 0;


 for(i=2;i<=x-1;i++){
   if (x % i == 0)return 0;
}
 return 1;

}