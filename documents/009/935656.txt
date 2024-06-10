#include<stdio.h>
#include<string.h>
#define LEN 100005

typedef struct pp{
  char name[100];
  int t;
}P;

P Q[LEN+1];
int head, tail, n;

void enqueue(P x){
  Q[tail]=x;
  if(tail>=LEN)tail=0;
  else tail++;
}

P dequeue(){
  P m;
  m=Q[head];
  if(head>=LEN)head=0;
  else head++;
  return m;
}


int main(){
  int elaps = 0, c;
  int i, q;
  P u;
  scanf("%d %d", &n, &q);
  for ( i = 1; i <= n; i++){
    scanf("%s", Q[i].name);
    scanf("%d", &Q[i].t);
  }
  head = 1;
  tail=n+1;
  while(head!=tail){
    if(Q[head].t>q){
      elaps+=q;
      Q[head].t-=q;
      enqueue(dequeue());
    }
    else{
      elaps+=Q[head].t;
      printf("%s %d\n",Q[head].name,elaps);
      dequeue();
      
    } 
  }
  return 0;
}