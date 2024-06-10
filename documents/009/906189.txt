#include<stdio.h>
#include<string.h>

int main(void)
{
  char str[20];
  int n,i;
  scanf("%s",str);
  n=strlen(str);
  i=n-1;
  while(i>=0){
    printf("%c",str[i--]);
  }
  printf("\n");
  return 0;
}