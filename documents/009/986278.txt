#include <stdio.h>

int main(void)
{
    int h, w;
    int i, j;

    while (1){
        scanf("%d %d", &h, &w);
        if (h == 0 && w == 0){
            break;
        }else{
            /*1行目*/
            for (j = 1;j <= w; j++){
                printf("#");
            }
            printf("\n");
            /*2 ~ (h -1) 行目*/
            for (i = 2; i <= h - 1; i++){
                printf("#");
                for (j = 2; j <= w - 1; j++){
                    printf(".");
                }
                printf("#\n");
            }
            /*h行目*/
            for (j = 1;j <= w; j++){
                printf("#");
            }
            printf("\n\n");
        }
    }

    return 0;
}