#include<stdio.h>

int main(void){
    int n,hoge,i,j,MAX=0,wa;
    long long int a[10000];
    while(scanf("%d",&n),n){
        for(i=0;i<n;i++){
            scanf("%lld",&a[i]);
        }
        MAX=a[0];
        for(i=0;i<n;i++){
            wa=a[i];
            for(j=i+1;j<n;j++){
                wa+=a[j];
                if(MAX<wa){
                MAX=wa;
                }
            }
        }
        printf("%d\n",MAX);
    }
    return 0;
}