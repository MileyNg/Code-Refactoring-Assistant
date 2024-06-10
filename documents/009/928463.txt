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
  Q[tail] = x;
  if(tail + 1 == LEN+1)tail = 0;
  else tail++;
}

P dequeue(){
  P a;
  a = Q[head];
  if(head + 1 == LEN + 1) head = 0;
  else head++;
  return a;
}

int isEmpty(){
  if(head == tail) return 1;
  else return 0;
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

  head =1;
  tail = n + 1;
  
  for(;;){
    u = dequeue();
    c = u.t - q;
    
    if(c > 0){
      elaps += q;
      u.t = c;
      enqueue(u);
    }
    
    else if(c <= 0){
      elaps += u.t;
      printf("%s %d\n", u.name, elaps);
    }

    if(isEmpty() == 1)break;
    else continue;
  }
  return 0;
}