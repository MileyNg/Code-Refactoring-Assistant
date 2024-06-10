#include<stdio.h>

main(){
  int a[2], b, c, tmp;
  int pre, res;
  int i;
  int min_b, min_c;
  int min, max;

  while(1){
    res = scanf("%d %d", &b, &c);

    if(res == EOF){
      break;
    }

    a[0] = b;
    a[1] = c;

    if(a[0] < a[1]){
      tmp = a[0];
      a[0] = a[1];
      a[1] = tmp;
    }

    while(1){
      pre = a[0] % a[1];

      if(pre == 0){
        max = a[1];
        break;
      }
      else{
        a[0] = a[1];
        a[1] = pre;
      }
    }

    min_b = b;
    min_c = c;

    while(1){
      if(min_b < min_c){
        min_b += b;
	continue;
      }

      if(min_c < min_b){
        min_c += c;
	continue;
      }

      if(min_c == min_b){
        min = min_c;
        break;
      }
    }

    printf("%d %d\n", max, min);
  }

  return 0;
}