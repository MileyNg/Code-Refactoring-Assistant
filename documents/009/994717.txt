#include<stdio.h>

int main(void)
{
  int n[30] = {0};
  int i = 0, j, k;
  int count[30] = {0};

  while(scanf("%d", &n[i]) != EOF){
    count[i] = 1;
    for(j=3; j<=n[i]; j++){
      for(k=2; k<j; k++){
	if(j % k == 0){
	  break;
	}
      }
      if(k == j){
      count[i]++;
      }
    }
    i++;
  }

  for(j=0; j<i; j++){
    printf("%d\n", count[j]);
  }

  return 0;
}