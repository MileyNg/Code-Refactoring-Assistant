#include<stdio.h>
#include<string.h>
int main(void){
    double a,b,c,d,e,f,output1,output2;
    while(scanf("%lf%lf%lf%lf%lf%lf",&a,&b,&c,&d,&e,&f)!=EOF){
        d=d*(b/e);
        f=f*(b/e);
        e=e*(b/e);
        output1=(c-f)/(a-d);
        output2=c-a*output1;
        output2=output2/b;
        printf("%.3f %.3f\n",output1,output2);
    }
    return 0;
}