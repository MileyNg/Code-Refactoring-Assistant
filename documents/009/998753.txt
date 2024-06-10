#include <stdio.h>

int main(void)
{
  int gyo, retu;
  int i, j;
  int Agyoretu[101][101];
  int bgyoretu[101];
  int tmp = 0;
  int answer[101] = {0};

  scanf("%d %d", &gyo, &retu);


  
  for(i = 0;i < gyo;i++){
    for(j = 0;j < retu;j++){
      scanf("%d ", &Agyoretu[i][j]);
    }
  }

  for(i = 0;i < retu;i++){
    scanf("%d ", &bgyoretu[i]);
  }
 
  for(i = 0;i < gyo;i++){
    tmp = 0;
    for(j = 0;j < retu;j++){
      tmp += Agyoretu[i][j] * bgyoretu[j];
    }
    answer[i] = tmp;
  }

  for(i = 0;i < gyo;i++){
    printf("%d\n", answer[i]);
  }

  return 0;
}