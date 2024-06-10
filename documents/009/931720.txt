#include<stdio.h>
int main(void){
    int i,datasets;
    scanf("%d",&datasets);
    for(i=0;i<datasets;i++){
        double x1,y1,x2,y2,x3,y3,x4,y4,a,b;
        scanf("%lf%lf%lf%lf%lf%lf%lf%lf"
              ,&x1,&y1,&x2,&y2,&x3,&y3,&x4,&y4);

        a=(y2-y1)/(x2-x1);
        b=(y4-y3)/(x4-x3);
        //printf("%lf\n",a);
        if(a==b){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }
    return 0;
}