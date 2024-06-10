#include<stdio.h>
int n,k,L,R,M;
int t[100000];

int check(int x){
  int i,id=0,cnt=0;
  for(i=0;i<n;i++){
    if(cnt+t[i]>x){
      cnt=t[i];
      id++;
    }else{
      cnt+=t[i];
    }
    if(id==k)return 0;
  } 
  return 1;
}

int main(){
  int i;
  scanf("%d %d",&n,&k);
  L=1;
  for(i=0;i<n;i++){
    scanf("%d",&t[i]);
    L=(L<t[i]?t[i]:L);
  }

  R=100000000;
  while(1){
    M=(L+R)/2;
    if(M==0||(check(M)==1&&check(M-1)==0)){
      break;
    }else if(check(M)==1){
      R=M+1;
    }else{
      L=M+1;
    }
  }
  printf("%d\n",M);
  return 0;
}