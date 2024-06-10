#include <stdio.h>

int main(void){
    int a[5000],s[5000],i,n,max_value;
    scanf("%d",&n);
    while(n > 0){
        for(i = 0; i < n; i++)
            scanf("%d",&a[i]);
        s[0] = a[0];
        for(i = 1; i < n; i++){
            s[i] = (s[i-1] > 0) ? (s[i-1] + a[i]) : a[i];
        }
        max_value = s[0];
        for(i = 1; i < n; i++){
            if(s[i] > max_value) max_value = s[i];
        }
        printf("%d\n",max_value);
        scanf("%d",&n);
    }
    return 0;
}