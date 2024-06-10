#include<stdio.h>
static const int N = 10000;

main(){
  int n, i;
  int numbers[N];
  
  scanf("%d", &n);

  for(i = 0; i < n; i++){
    scanf("%d", &numbers[i]);
  }

  printf("%d\n", primary(numbers, n));
  return 0;
}

int primary(int numbers[], int n){
  int i, j, divisora, prime = 0;
  for(i = 0; i < n; i++){
    divisora = 0;
    if(numbers[i] != 2){
      if(numbers[i] % 2 == 0){
	divisora++;
      } else {
        for(j = 3; j < numbers[i]; j += 2){
	  if(numbers[i] % j == 0){
	    divisora++;
	    break;
	  }
        }
      }
    }
    if(divisora == 0){
       prime++; 
    }
  }
  return prime;
}