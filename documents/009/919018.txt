#include<stdio.h>

main(void){
    int money = 100000, num;
    double moneyDouble;
    
    scanf("%d", &num);
    
    for( ; num >= 0; num--){
        money += money * 0.05;
    }
    
    moneyDouble = money / 10000;
    money = (moneyDouble + 0.9);
    money = money * 10000;
    
    printf("%d\n", money);

    return 0;
}