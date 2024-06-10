#include<stdio.h>
int main(void){
    int i,n,money=100000;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        money*=1.05;
        money+=999;
        money-=money%1000;
    }
    printf("%d\n",money);
    return 0;
}