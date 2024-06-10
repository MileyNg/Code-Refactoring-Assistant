#include<stdio.h>

int sum(int *p,int i,int n){
  if(i==n){
    return 0;
  }
  else{
    return p[i]+sum(p,i+1,n);
  }
}

int max(int *p,int i,int n,int m){
  if(i==n){
    return m;
  }
  else{
    int tmp;
    if(p[i]>m){
      tmp=p[i];
    }
    else{
      tmp=m;
    }
    return max(p,i+1,n,tmp);
  }
}

int min(int *p,int i,int n,int m){
  if(i==n){
    return m;
  }
  else{
    int tmp;
    if(p[i]<m){
      tmp=p[i];
    }
    else{
      tmp=m;
    }
    return min(p,i+1,n,tmp);
  }
}

void doit(){
  int n;
  scanf("%d",&n);
  if(n!=0){
    int sc[n];
    int i;
    int ans;
    for(i=0;i<n;i++){
      scanf("%d",&sc[i]);
    }
    ans=(sum(sc,0,n)-max(sc,0,n,0)-min(sc,0,n,1000))/(n-2);
    printf("%d\n",ans);
    doit();
  }
}

int main(){
  doit();
  return 0;
}