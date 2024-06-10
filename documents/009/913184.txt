#include<stdio.h>
int main(void){
    double a,b,c,d,e,f,output1,output2;
    while(scanf("%lf%lf%lf%lf%lf%lf",&a,&b,&c,&d,&e,&f)!=EOF){
        output1=(c*e-b*f)/(a*e-b*d);
        output2=(c*d-a*f)/(b*d-a*e);
        printf("%.3f %.3f\n",output1,output2);
    }
    return 0;
}