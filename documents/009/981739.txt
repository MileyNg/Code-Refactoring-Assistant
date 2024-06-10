#include <stdio.h>
#include <string.h>
main(){
  char str[20],tmp,a;
  int i,j,ch;
  while(scanf("%s",str)!=EOF){
    ch=strlen(str);
    for(i=0;i<ch;i++){
      for(j=ch-1;j>i;j--){
	tmp=str[j];
	str[j]=str[j-1];
	str[j-1]=tmp;
      }
    }
    printf("%s\n",str);
  }
  return 0;
}