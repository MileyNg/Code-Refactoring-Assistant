#include<stdio.h>
#include<limits.h>

static const int MAX = 500;
static const int INFTY = (1 << 21);

/*

 */
int solve(int s, int e) {
    
}

int main(void) {
    int n, i, j, e, sum;
    short M[MAX][MAX];
    int p[MAX];

    scanf("%d\n", &n);
    for (i = 1; i <= n; i++) {
        p[i] = INT_MAX;
    }

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            scanf("%d", &e);
            M[i][j] = (e == -1) ? INFTY : e;
            
            if(p[j] > e && e >= 0) {
                p[j] = e;
            }
        }
    }

    sum = 0;
    
    p[1] = 0;

    for (i = 1; i <= n; i++) {      
        if (p[i] != -1) sum += p[i];
    }

    printf("%d\n", sum);

    return 0;
}