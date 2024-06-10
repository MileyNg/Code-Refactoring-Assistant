#include<stdio.h>

/*最大公約数を返す関数*/
int GCD(int a,int b){
  int i;
  int n1, n2;
  int ans;
  n1 = (a > b) ? a : b;
  n2 = (a > b) ? b : a;
  // n1 > n2である
  if(n1%n2 == 0){
    ans = n2;
  }
  else{
    for(i=1; i<n2/2; i++){ //n2/2までで良いと思う
      if(n1%i == 0 && n2%i == 0) ans = i;
    }
  }
  return ans;
}

/*最小公倍数を返す関数*/
int LCM(int a,int b){
  int i,j,k=1;
  int n1, n2;
  int ans;
  n1 = (a > b) ? a : b;
  n2 = (a > b) ? b : a;
  // n1 > n2である
  for(i=1;i<=n2;i++){
    for(j=k;j<=n1;j++){
      k++;
      if((n1*i) == (n2*j)){
	return (n1*i);
      }
      if((n1*i) < (n2*j)){
	break;
      }
    }
  }
}
int main(){
  int a,b;

  while(scanf("%d %d",&a ,&b) != EOF){
    printf("%d %d\n",GCD(a,b), LCM(a,b));
  }
  return 0;
}