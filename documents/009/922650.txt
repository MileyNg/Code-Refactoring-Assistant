#include<stdio.h>
#include<string.h>
int main(void){
   char str[100],rts[100];
   int i,j,work;

   while((scanf("%s",str))!=EOF){
      for(i = strlen(str)-1;i>=0;i--){
         printf("%c",str[i]);
      }
      puts("");
   }
   return 0;
}