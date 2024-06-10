#include<stdio.h>
#include<string.h>
#define LEN 100005

typedef struct pp{
  char name[100];
  int t;
}P;

P Q[LEN];
int head=0, tail, n;

void enqueue(P x){
  strcpy(Q[tail].name,x.name);
  Q[tail].t = x.t;
  tail++;
  if(tail == LEN){
    tail = 0; 
  }
}




int main(){
  int elaps = 0;
  int i, q;
  P u;
  scanf("%d %d", &n, &q);

  for ( i = 0; i < n; i++){
    scanf("%s", Q[i].name);
    scanf("%d", &Q[i].t);
  }
  tail = n;

  while(tail!=head){
    if(Q[head].t > q){
      elaps += q;
      Q[head].t -= q;
      enqueue(Q[head]);

    }
    else{
      elaps+=Q[head].t; 
      printf("%s %d\n",Q[head].name,elaps);

    }
    head++;
    if(head == LEN){
      head = 0;
    }
  }  
  return 0;
}