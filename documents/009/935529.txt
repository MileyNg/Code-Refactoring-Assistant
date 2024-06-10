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
  tail++;
  if(tail == LEN+1) tail=0;
}

P dequeue(){
  P  de=Q[head];
  if(head != LEN) head++;
  if(head == LEN+1) head=0;
         return de;

}


int main(){
  int elaps = 0, c;
  int i, q;
  P u;
  scanf("%d %d", &n, &q);

  for ( i = 1; i <= n; i++){
    scanf("%s", Q[i].name);
    scanf("%d", &Q[i].t);
    enqueue(Q[i]);
  }

  while(tail-head > 0){
    if(Q[head].t > q){
      Q[head].t=Q[head].t-q;
      elaps+=q;
      enqueue(Q[head]);
      dequeue();

    }
 else{
      elaps+=Q[head].t;
      Q[head].t=elaps;

      printf("%s %d\n",Q[head].name,Q[head].t);
      dequeue();

    }

  }
return 0;
  
}