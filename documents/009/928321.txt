#include<stdio.h>
#include<string.h>
#define LEN 100005

typedef struct pp{
  char name[100];
  int t;
}P;
int head=0, tail, n;
void enqueue(P x);

P Q[LEN+1];
int main(){
  int elaps = 0, c=0;
  int i, q;
  
  scanf("%d %d", &n, &q);
  tail=n;
  for ( i = 0; i < n; i++){
    scanf("%s", Q[i].name);
    scanf("%d", &Q[i].t);
    c+=Q[i].t;
  }
  while(elaps - c !=0){
      if(   Q[head].t>q   ){
	Q[head].t-=q;
	elaps+=q;
	enqueue(Q[head]);
      }
      else {
	elaps+=Q[head].t;
	printf("%s %d\n",Q[head].name,elaps);
      }
      head++;
      if(tail==LEN+1)tail=0;
  }
  return 0;
}
void enqueue(P x){
  strcpy(Q[tail].name,x.name);
  Q[tail].t=x.t;
  tail++;
  if(tail==LEN+1)tail=0;
}