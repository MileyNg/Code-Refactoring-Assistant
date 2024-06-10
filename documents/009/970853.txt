#include<stdio.h>

int gcd(int a,int b){
  if(a==b){
    return a;
  }
  else if(a>b){
    return gcd(b,a);
  }
  else{
    return gcd(a,b-a);
  }
}

int main(){
  int a,b;

  while(scanf("%d %d",&a,&b)!=EOF){
    int x=gcd(a,b);
    int y=(a/x)*b;

    printf("%d %d\n",x,y);
  }

  return 0;
}