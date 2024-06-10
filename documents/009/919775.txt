#include <stdio.h>
#define ERROR_RANGE 0.000001
int main(void){
    int cnt,flg;
    double x1,y1,x2,y2,x3,y3,x4,y4;
    scanf("%d",&cnt);
    while(cnt-- > 0){
        scanf("%lf %lf %lf %lf %lf %lf %lf %lf",
               &x1,&y1,&x2,&y2,&x3,&y3,&x4,&y4);
        if( (x1 - x2) < ERROR_RANGE || (x3 - x4) < ERROR_RANGE ){
            flg = ((x1 - x2) < ERROR_RANGE && (x3 - x4) < ERROR_RANGE);
        }else{
            flg = ((y1 - y2)*100000/(x1 - x2) - (y3 - y4)*100000/(x3 - x4)) < ERROR_RANGE;
        }
        if(flg){
            puts("YES");
        }else{
            puts("NO");
        }
    }
    return 0;
}