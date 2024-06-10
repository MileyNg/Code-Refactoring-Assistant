#include<stdio.h>
#define N 32769

int prime[N];

int ertstns(){
  int i;
  int cnt=0;
  for(i=0;i<N;i++){
    if(i<2){
      prime[i]=0;
    }
    else{
      prime[i]=1;
    }
  }
  for(i=2;i<N;i++){
    int j;
    for(j=2*i;j<N;j+=i)
      prime[j]=0;
  }
  for(i=0;i<N;i++){
    if(prime[i]==1){
      cnt++;
    }
  }
  return cnt;
}

void gldbch(int *p,int n){
  int i;
  int cnt=0;
  for(i=0;p[i]<=n/2;i++){
    int j=i;
    int f=0;
    while((p[j]<=n)&&(f==0)){
      if((p[i]+p[j])==n){
	cnt++;
	f=1;
      }
      j++;
    }
  }
  printf("%d\n",cnt);
}

void doit(){
  int m=ertstns();
  int i;
  int prm[m];
  int j=0;
  int n;
  i=0;
  for(i=0;i<N;i++){
    if(prime[i]==1){
      prm[j]=i;
      j++;
    }
  }
  scanf("%d",&n);
  while(n!=0){
    gldbch(prm,n);
    scanf("%d",&n);
  }
}

int main(){
  doit();
  return 0;
}