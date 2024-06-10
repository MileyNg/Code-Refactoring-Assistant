#include <stdio.h>
 
int main(void){
    int n, i;
    int sum = 100000;
     
    scanf("%d", &n);
     
    for (i = 0; i < n; i++){
        sum += sum * 0.05;
    }
     
    if (sum % 1000 > 0){
        sum /= 10000;
        sum *= 10000;
        sum += 10000;
    }
     
    printf("%d\n", sum);
    
	return (0);
}