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
     if(tail == LEN){
       tail = 0;         
     } else {
       tail++;
     }
     Q[tail] = x;
}     
 
P dequeue(){
     if(head == LEN){
       head = 0;
return Q[LEN -1]; 
     } else {
       head++;
     }
return Q[head-1];
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
  
  tail = n;
  head = 1;
 
  while(tail >= head){    
    if(Q[head].t > q){
      elaps += q;
      Q[head].t -= q; 
      enqueue(dequeue());
 
    } else {
      elaps += Q[head].t;
      dequeue();
      printf("%s %d\n", Q[head-1].name, elaps);
    }
  }
   
  return 0;
}