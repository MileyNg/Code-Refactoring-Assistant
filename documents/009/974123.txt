#include<stdio.h>

void playit(char *y,int *t,int b,int i,int n){
  int a[n];
  int j;
  for(j=0;j<n;j++){
    a[j]=t[j];
  }

  if(i==100){
    for(j=0;j<n;j++){
      int k;
      for(k=j+1;k<n;k++){
	if(a[k]<a[j]){
	  int tmp=a[k];
	  a[k]=a[j];
	  a[j]=tmp;
	}
      }
    }
    for(j=0;j<n;j++){
      printf("%d ",a[j]);
    }
    printf("%d\n",b);
  }
  else{
    int bn;
    a[i%n]++;
    if(y[i]=='S'){
      bn=b+a[i%n];
      a[i%n]=0;
    }
    else if(y[i]=='L'){
      a[i%n]+=b;
      bn=0;
    }
    else if(y[i]=='M'){
      bn=b;
    }
    playit(y,a,bn,i+1,n);
  }
}

void bonze(int n){
  char yama[101];
  int te[n];
  int i;

  scanf("%s",yama);
  for(i=0;i<n;i++){
    te[i]=0;
  }
  playit(yama,te,0,0,n);
}

void doit(){
  int n;
  scanf("%d",&n);
  if(n!=0){
    bonze(n);
    doit();
  }
}

int main(){
  doit();
  return 0;
}