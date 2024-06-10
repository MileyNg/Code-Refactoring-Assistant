#include <stdio.h>

int main(void)
{
  int kazu;
  int suchi[10001];
  int i;
  long min, max, sum;

  scanf("%d", &kazu);
  
  for(i = 0;i < kazu;i++){
    scanf("%d", &suchi[i]);
  }

  min = 1000000;
  for(i = 0;i < kazu;i++){
    if(min > suchi[i]){
      min = suchi[i];
    }
  }

  max = -1000000;
  for(i = 0;i < kazu;i++){
    if(max < suchi[i]){
      max = suchi[i];
    }
  }

  sum = 0;
  for(i = 0;i < kazu;i++){
    sum += suchi[i];
  }

  printf("%ld %ld %ld\n", min, max, sum);

  return 0;
}