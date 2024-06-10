#include<stdio.h>
#include<ctype.h>
 
int main(){
  char b[100000];
  int i=0,c;
   
  while(1){
    c=getchar();
 
    if(c=='\n')
      break;
 
    if(islower(c))
      b[i++]=toupper(c);
    else if(isupper(c))
      b[i++]=tolower(c);
    else
      b[i++]=c;
  }
  b[i]='\0';
  printf("%s\n",b);
  return 0;
}