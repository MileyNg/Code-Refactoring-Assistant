#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, const char * argv[])
{
    int a,b,c,i,x;
    char Str[128] = "";
    char *t;
    for (i = 0; i < 3; i++) {
        c = 0;
        fgets(Str, 128, stdin);
        t = strtok(Str, " ");
        a = atoi(t);
        t = strtok(NULL, "\n");
        b = atoi(t);
        x = a+b;
        while(x > 0){
            c++;
            x = x/10;
        }
        printf("%d\n",c);
    }
    return 0;
}