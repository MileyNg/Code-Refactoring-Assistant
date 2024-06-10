#include <stdio.h>

int main(int argc, const char * argv[])
{
    int i, j, k, datasets, max;
    int side[3];
    int num[2];
    int a, b, c;
    
    scanf("%d", &datasets);

    for (i = 0; i < datasets; i++) {
        scanf("%d %d %d", &side[0], &side[1], &side[2]);
        
        for (j = 1, max = 0; j < 3; j++) {
            if(side[max] < side[j]) {
                max = j;
            }
        }
        
        for (j = 0; j < 3; j++) {
            if(side[j] != side[max]) {
                num[k++] = j;
            }
        }

        c = side[max] * side[max];
        a = side[num[0]] * side[num[0]];
        b = side[num[1]] * side[num[1]];
        
        if (c == (a + b)) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }

    return 0;
}