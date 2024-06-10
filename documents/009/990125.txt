#include<stdio.h>
int main(){

  double a,b,c,d,e,f;
  while(scanf("%lf %lf %lf %lf %lf %lf",&a,&b,&e,&c,&d,&f)!=EOF){
    //printf("%f,%f,%f,%f,%f,%f\n",a,b,c,d,e,f);
    double x=0,y=0;
    x=(d*e-b*f)/(a*d-b*c);
    y=(a*f-c*e)/(a*d-b*c);
    printf("%.3f %.3f\n",x,y);
  }
    return 0;
}