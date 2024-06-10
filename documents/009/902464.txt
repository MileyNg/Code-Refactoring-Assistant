#include<stdio.h>

main(){
  int a[3], num;
  int i, tmp, cnt = 0;
  int sum, last;

  scanf("%d", &num);

  while(cnt < num){
    scanf("%d %d %d", &a[0], &a[1], &a[2]);

    last = 2;
    while(last > 0){
      for(i = 0 ; i < last ; i++){
        if(a[i] < a[i + 1]){
          tmp = a[i];
          a[i] = a[i+1];
          a[i+1] = tmp;
        }
      }
      last--;
    }

    a[0] *= a[0];
    sum = a[1]*a[1] + a[2]*a[2];

    if(sum == a[0]){
      printf("YES\n");
    }
    else{
      printf("NO\n");
    }

    cnt++;
  }
  return 0;
}