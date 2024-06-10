#include<stdio.h>
int main(){
    int n,count=0,m=0,i,j;
    while(scanf("%d",&n)!=EOF){
        for(i=2;i<=n;i++){
            for(j=1;j<i;j++){
                if(i%j==0)count++;
            }
            if(count==1)m++;
            count=0;
        }
        printf("%d\n",m);
        m=0;
    }
    return 0;
}