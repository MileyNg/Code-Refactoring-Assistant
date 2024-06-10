#include<stdio.h>
int main (void){
 int a,b,n,i,j;
for(j=0;j<3;j++){
 scanf("%d",&a);
 scanf("%d",&b);
 n=a+b;i=1;
 while(9<n){
  n/=10;i++;
 }
printf("%d\n",i);
}

return 0;
}