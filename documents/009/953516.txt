#include<stdio.h>

/* 桁数を返す関数 */
int digitNumber(int n);

/* main関数 */
int main(){
  int i;
  int a, b;
  int digitnum;

  while(scanf("%d %d",&a,&b) != EOF){
    digitnum = digitNumber(a+b);
    printf("%d\n",digitnum);
  }

  return 0;
}

int digitNumber(int n){
  //nを0になるまでひたすら割る.
  //割った回数が桁数である。
  int cnt = 1;

  while((n/10) != 0){
    cnt ++;
    n = n/10;
  }

  return cnt;
}