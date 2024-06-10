#include <stdio.h>

int main()
{
    int a,b;
    char Str[16];
    while(scanf("%d %d",&a,&b) != EOF){
        printf("%d\n",sprintf(Str,"%d",a+b));
    }
    return 0;
}