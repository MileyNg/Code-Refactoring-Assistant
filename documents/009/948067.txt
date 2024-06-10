#include <stdio.h>

#define MAX 100000
typedef long long ll;

int check(ll,int*,int,int);

int main(){
  int n,k,w[MAX],i;
  ll lb,ub,mid;

  scanf("%d%d" ,&n ,&k);
  for(i = 0 ; i < n ; i++){
    scanf("%d" ,&w[i]);
  }

  lb = 0, ub = 10000000001LL;
  while(ub - lb > 0){
    mid = (lb + ub) / 2;

    if(check(mid,w,n,k)){
      ub = mid;
    }else{
      lb = mid+1;
    }
  }
  printf("%lld\n" ,ub);

  return 0;
}

int check(ll limit,int w[],int n,int k){
  int i,kk = 0;
  ll sum = 0;

  for(i = 0 ; i < n ; i++){
    sum += w[i];

    if(sum == limit){
      kk++;
      sum = 0;
    }else if(sum > limit){
      kk++;
      sum = w[i];
    }
  }
  if(sum > 0){
    kk++;
  }

  return kk <= k;
}