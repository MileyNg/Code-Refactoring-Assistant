#include <stdio.h>
 
int main(){
    double a,b,c,d,e,f,A;
    double x,y;
    double AA[2][2];
 
    for(;scanf("%lf %lf %lf %lf %lf %lf",&a,&b,&c,&d,&e,&f) == 6;){
        A = a*e-b*d;
        AA[0][0] = e/A;
        AA[0][1] = -b/A;
        AA[1][0] = -d/A;
        AA[1][1] = a/A;
        x = c*AA[0][0]+f*AA[0][1];
        y = c*AA[1][0]+f*AA[1][1];
        printf("%.3f %.3f\n",x,y);
    }
 
    return 0;
}