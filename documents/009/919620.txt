#include <stdio.h>

int main(){
  
  char s[100],*p;
  
  scanf("%s",s);
  p = s;
  do{
    p++;  
  }while(*p != '\0');
  
  do{
    p--;
    printf("%c",*p);
  }while(p != s);
  printf("\n");
  return 0; 

}