#include<stdio.h>
int main(void)
{
  char moji;
   
  while(1){
      scanf("%c",&moji);
       
      if(moji >= 'A' && moji <= 'Z'){
    moji += 32;
    printf("%c",moji);
      }
       
      else if(moji >= 'a' && moji <= 'z'){
    moji -= 32;
    printf("%c",moji);
      }
       
      else if(moji != '\n'){
    printf("%c",moji);
      }
      else if(moji == '\n'){
    printf("\n");
    break;
      }
  }
  return 0;
}