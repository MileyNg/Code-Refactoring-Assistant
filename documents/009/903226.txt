#include <stdio.h>

int main(){
  int i, j, k, l;
  int num;
  int count = 0;
  int res;

  while(1){
  res = scanf("%d", &num);

  if(res == EOF) break;

  if(num < 36){
    for(i = 0 ; i <= 9 ; i++){
      for(j = 0 ; j <= 9 ; j++){
        for(k = 0 ; k <= 9 ; k++){
          for(l = 0 ; l <= 9 ; l++){
            if(i + j + k + l == num){
              count++;
	    }
          }
        }
      }
    }
  }

  printf("%d\n", count);
  count = 0;
  }
  return 0;
}