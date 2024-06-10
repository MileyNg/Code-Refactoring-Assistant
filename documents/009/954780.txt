#include<stdio.h>
 
int main(void){
    double a,b,c,d,e,f,g,x,y;
 
    while(scanf("%lf%lf%lf%lf%lf%lf",&a,&b,&c,&d,&e,&f)!=EOF){
        y=(f-c*d/a)/(e-b*d/a);
        x=(f-c*e/b)/(d-a*e/b);
 
        if(-0.0004<x&&x<=0)x=0;
        if(-0.0004<y&&y<=0)y=0;
 
        printf("%.3f %.3f\n",x,y);
     
    }
 
    return 0;
 
}