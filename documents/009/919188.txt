#include <stdio.h>

int main(void){
    int cnt,flg;
    double x1,y1,x2,y2,x3,y3,x4,y4,ABx,ABy,CDx,CDy;
    scanf("%d",&cnt);
    while(cnt-- > 0){
        scanf("%lf %lf %lf %lf %lf %lf %lf %lf",
               &x1,&y1,&x2,&y2,&x3,&y3,&x4,&y4);
        ABx = x1 - x2;
        ABy = y1 - y2;
        CDx = x3 - x4;
        CDy = y3 - y4;
        if( ABx == 0 || CDx == 0){
            flg = (ABx == CDx);
        }else if( ABy == 0 || CDy == 0){
            flg = (ABy == CDy);
        }else{
            flg = (ABx * CDy == ABy * CDx);
        }
        if(flg){
            puts("YES");
        }else{
            puts("NO");
        }
    }
    return 0;
}