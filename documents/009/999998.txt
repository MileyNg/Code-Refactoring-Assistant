#include <stdio.h>

int main(){
    
    int i, n, debt;
    
    debt = 100000;
    scanf("%d", &n);
    
    for (i = 0; i < n; i++) {
        debt *= 1.05;
        if (debt % 1000) {
            debt = (debt / 1000 + 1) * 1000;
        }
    }
    printf("%d\n", debt);

    return 0;
}