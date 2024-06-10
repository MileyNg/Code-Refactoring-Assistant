#include<stdio.h>
#include<string.h>
int main(void){
    char str[20],copy_str[20];
    int count_str,i,j;
    scanf("%s",str);
    count_str=strlen(str);
    for(i=0,j=count_str;i<count_str;i++,j--){
        copy_str[i]=str[j-1];
    }
    copy_str[count_str]='\0';
    printf("%s\n",copy_str);
    return 0;
}