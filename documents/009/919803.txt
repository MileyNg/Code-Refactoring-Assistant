#include<stdio.h>
int main(){
int i,n;
double a[2],b[2],c[2],d[2];
scanf("%d",&n);
for(i=0;i<n;i++){
scanf("%lf%lf%lf%lf%lf%lf%lf%lf",&a[0],&a[1],&b[0],&b[1],&c[0],&c[1],&d[0],&d[1]);
if((b[1]-a[1])*(d[0]-c[0])==(b[0]-a[0])*(d[1]-c[1]))
printf("YES\n");
else
printf("NO\n");
}
return 0;
}