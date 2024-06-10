#include <stdio.h>

int main(void)
{
    int min, middle, max;
    int sum;
    int n, x;
    int cnt;

    while (1){
        scanf("%d %d", &n, &x);
        if (n == 0 && x == 0){
            break;
        }else{
            cnt = 0;
            for (min = 1; min <= (x / 3); min++){
                for (middle = min + 1; middle < (x - min) / 2.0; middle++){
                    /*max = x - min - middle > middle => middle < (x - min) / 2*/
                    for (max = middle + 1; max <= n; max++){
                        sum = min + middle + max;
                        if (sum == x){
                            cnt++;
                        }
                    }
                }
            }
            printf("%d\n", cnt);
        }
    }

    return 0;
}