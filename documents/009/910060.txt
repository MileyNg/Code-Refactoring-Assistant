#include <stdio.h>

int main()
{
  int sei[10000], N, i, j, count = 0;
  scanf("%d", &N);
  for(i = 0; i < N; i++){
    scanf("%d", &sei[i]);
  }
  for(i = 0; i < N; i++){ 
    if(sei[i] == 2) count += 1;
    for(j = 2; j < sei[i]; j++){
      if(sei[i] % j == 0) break;;
      if(j == sei[i] - 1) count += 1;
    }
  }
  printf("%d\n", count);
  return 0;
}