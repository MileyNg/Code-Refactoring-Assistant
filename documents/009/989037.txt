#include <stdio.h>

int main(void)
{
    int i;
    char in_str[1000];
    int in_num;
    int sum;

    while (1){
        sum = 0;
        scanf("%s", in_str);
        if (in_str[0] == '0'){
            break;
        }else{
            for (i = 0; i < 1000; i++){
                if (in_str[i] == '\0'){
                    break;
                }else{
                    in_num = in_str[i] - '0';
                    sum += in_num;
                }
            }
            printf("%d\n", sum);
        }
    }

    return 0;
}