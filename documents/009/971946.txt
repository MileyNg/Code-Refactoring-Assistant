#include<stdio.h>

int a[3]={3600,60,1};

int scnd(int h,int m,int s){
  int inpt[3]={h,m,s};
  int i;
  int n=0;
  for(i=0;i<3;i++){
    n=n+a[i]*inpt[i];
  }

  return n;
}

int lefttape(int h,int m,int s,int f){
  int scd=scnd(h,m,s);
  int t;
  if(f==0){
    t=1;
  }
  else{
    t=3;
  }

  return t*(7200-scd);
}

int whttm(int s,int f){
  if(f/3==0){
    return s/a[f%3];
  }
  else{
    return s%a[f%3];
  }
}

void ans(int h,int m,int s){
  int answer[6];
  int i;
  for(i=0;i<2;i++){
    int sc=lefttape(h,m,s,i);
    int j;
    for(j=0;j<3;j++){
      answer[i*3+j]=whttm(sc,j);
      sc=whttm(sc,j+3);
    }
  }
  for(i=0;i<6;i++){
    if(answer[i]<10){
      printf("0");
    }
    printf("%d",answer[i]);
    if(i%3==2){
      printf("\n");
    }
    else{
      printf(":");
    }
  }
}

void doit(){
  int h,m,s;
  scanf("%d %d %d",&h,&m,&s);
  if(h!=-1){
    ans(h,m,s);
    doit();
  }
}

int main(){
  doit();
  return 0;
}