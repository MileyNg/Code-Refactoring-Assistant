#include<stdio.h>
#include<string.h>
main(){
  char str[21],tmp;
  int n,i,j,k;
  scanf("%s",str);
  n=strlen(str);
  for(i=0;i<n;i++){
    for(j=n-1;j>i;j--){
      tmp=str[j];
      str[j]=str[j-1];
      str[j-1]=tmp;
    }
  }
  printf("%s\n",str);
  return 0;
}
 