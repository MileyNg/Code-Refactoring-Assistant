#include<stdio.h>
#include<string.h>
#define LEN 100005

typedef struct pp{
  char name[100];
  int t;
}P;

P Q[LEN+1];
int head=1, tail=0, n;

void enqueue(P x){
  Q[tail]=x;
  tail++;
}

void dequeue(){
  head++;
}


int main(){
  int i=1, q;
  int time=0;
  scanf("%d %d", &n, &q);
  tail=n+1;

  for ( i = 1; i <= n; i++){
    scanf("%s", Q[i].name);
    scanf("%d", &Q[i].t);
  }
  i=1;

  while(1){
    if(Q[i].t-q <= 0){
      time += Q[i].t;
      printf("%s %d\n",Q[i].name,time);
      dequeue();
    }
    else{
      time += q;
      Q[i].t -= q;
      enqueue(Q[i]);
      head++;
    }
    if(head==tail)
      break;
    i++;
  }
  
  return 0;
}