#include<stdio.h>
 
double h(double x1,double y1,double x2,double y2){
    if((x1-x2)==0)return 65535;
    else return (y1-y2)/(x1-x2);
}
 
int main(){
    int i,j,n;
    double x[4],y[4],ab,cd;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        for(j=0;j<4;j++)scanf("%lf%lf",&x[j],&y[j]);
        ab=h(x[0],y[0],x[1],y[1]);
        cd=h(x[2],y[2],x[3],y[3]);
        if(ab==cd)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}