#include <stdio.h>
#include<string.h>
#define LEN 100001
  
typedef struct pp{
    char name[100];
    int t;
}P;
  
P Q[LEN+1];
int head = 1, tail = 0, n, empty = 0;
  
void push(P x){
    empty++;
    Q[++tail] = x;
    tail %= LEN;
}
  
P pop(){
    P res;
    empty--;
    res = Q[head++];
    head %= LEN;
    return res;
}
  
  
int main(){
    int time = 0, count = 0;
    int i, ms;
    P u;
    scanf("%d %d", &n, &ms);
  
    empty = n;
    tail = n;
  
    for ( i = 1; i <= n; i++){
        scanf("%s", Q[i].name);
        scanf("%d", &Q[i].t);
    }
  
    while(empty != 0){
  
        u = pop();
        if(u.t <= ms) {
            time += u.t;
            printf("%s %d\n", u.name, time);
        }
  
        else if(u.t > ms){
            time += ms;
            u.t -= ms;
            push(u);
        }
        else if(u.t == 0) continue;
    }
  
  
    return 0;
}