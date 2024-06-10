#include<stdio.h>
#include<math.h>
#define E 0.00000001

int iszr(double x){
  if(fabs(x)<E){
    return 1;
  }
  else{
    return 0;
  }
}

double a(double x1,double x2,double y1,double y2){
  return (y1-y2)/(x1-x2);
}

double b(double x1,double x2,double y1,double y2){
  return (x1*y2-x2*y1)/(x1-x2);
}

double c(double p,double x,double y){
  return y+x/p;
}

double xa(double p,double q,double r){
  return (r-q)/(p+1/p);
}

double ya(double p,double q,double r){
  return r+(q-r)/(p*p+1);
}

void doit(double x1,double y1,double x2,double y2,double xq,double yq){
  double x,y;
  if(iszr(x1-x2)==1){
    x=2.00000000*x1-xq;
    y=yq;
  }
  else if(iszr(y1-y2)==1){
    x=xq;
    y=2.00000000*y1-yq;
  }
  else{
    double p=a(x1,x2,y1,y2);
    double q=b(x1,x2,y1,y2);
    double r=c(p,xq,yq);
    double xp=xa(p,q,r);
    double yp=ya(p,q,r);
    x=2.00000000*xp-xq;
    y=2.00000000*yp-yq;
  }
  printf("%f %f\n",x,y);
}

int main(){
  double x1,y1,x2,y2,xq,yq;
  while(scanf("%lf,%lf,%lf,%lf,%lf,%lf",&x1,&y1,&x2,&y2,&xq,&yq)!=EOF){
    doit(x1,y1,x2,y2,xq,yq);
  }
  return 0;
}