#include <stdio.h>
#include <string.h>

#define MAX 100000

typedef struct{
  char name[11];
  int time;
} queue;

queue Q[MAX];
int used[MAX];

int main(){
  int n,q,i,empty,p = 0,sum = 0;

  scanf("%d %d" ,&n ,&q);
  for(i = 0 ; i < n ; i++){
    scanf("%s %d" ,Q[i].name ,&Q[i].time);
    used[i] = 1;
  }

  empty = n;
  while(empty != 0){
    if(!used[p]){
      p++;
      if(p == n) p = 0;
      continue;
    }
    if(Q[p].time > q){
      Q[p].time -= q;
      sum += q;
    }else{
      sum += Q[p].time;
      Q[p].time = 0;

      used[p] = 0;
      empty--;
      printf("%s %d\n" ,Q[p].name, sum);
    }
   
    p++;
    if(p == n){
      p = 0;
    }
  }

  return 0;
}