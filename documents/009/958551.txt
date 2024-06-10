#include <stdio.h>
#define MAX 1000000
int prime_count[MAX];
int main(void){
  int n = 0, i, j;
 
  for(i = 2; i < MAX; ++i){
    if(prime_count[i] != -1){
      for(j = i * 2; j < MAX; j += i){
        prime_count[j] = -1;
      }
      prime_count[i] = ++n;
    }else{
      prime_count[i] = n;
    }
  }
 
  while(scanf("%d", &n) != EOF){
    printf("%d\n", prime_count[n]);
  }
  return 0;
}