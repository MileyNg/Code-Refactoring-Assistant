#include<stdio.h>
#include<string.h>
#define LEN 100005

typedef struct pp{
  char name[100];
  int t;
}P;

P Q[LEN+1];
int head=0, tail=0, n;

void enqueue(P x){
  Q[tail]=x;
  if(tail+1==LEN){
    tail=0;
  } else {
    tail=tail+1;
  }
}

P dequeue(){
  P x=Q[head];
  if(head+1==LEN){
    head = 0;
  } else {
    head=head+1;
  }
  return x;
}


int main(){
  int elaps = 0, c;
  int i, q;
  P u;
  scanf("%d %d", &n, &q);

  for ( i = 0;i < n; i++){
    scanf("%s", u.name);
    scanf("%d", &u.t);
    enqueue(u);
    
  }
  while(tail != head){
    u=dequeue();
    if(u.t<=100){
      elaps+=u.t;
      printf("%s %d\n",u.name,elaps);
    } else {
      u.t-=100;
      elaps+=100;
      enqueue(u);
      
    }
  }
  
  return 0;
}