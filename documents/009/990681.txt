#include <stdio.h>

int main(void)
{
    int i;
    int n;
    int in_i;

    scanf("%d", &n);
    int in[n], out[n];

    for (i = 0; i < n; i++){
        scanf("%d", &in_i);
        in[i] = in_i;
    }

    for (i = 0; i < n; i++){
        out[i] = in[n - 1 - i];
    }

    for (i = 0; i < n; i++){
        if (i){
            printf(" ");
        }
        printf("%d", out[i]);
    }
    printf("\n");

    return 0;
}