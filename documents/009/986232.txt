#include <stdio.h>

int main(void)
{
    int a, b;
    char op;
    int result;

    while (1){
        scanf("%d %c %d", &a, &op, &b);
        if (op == '+'){
            result = a + b;
        }else if (op == '-'){
            result = a - b;
        }else if (op == '*'){
            result = a * b;
        }else if (op == '/'){
            result = a / b;
        }else if (op == '?'){
            break;
        }else{
            printf("ERROR!\n");
        }

        printf("%d\n", result);
    }

    return 0;
}