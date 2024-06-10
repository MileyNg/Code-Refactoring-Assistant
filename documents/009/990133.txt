#include<stdio.h>
#include<string.h>
int main(){
  char str[21],tmp[21];
  int a,i,j,x=0;
  scanf("%s",str);
  x = strlen(str);
  for(i=0;i<=x;i++){
    if(i==x){
      tmp[i] = str[i];
    }
    else{
      tmp[x-1-i] = str[i];
    }
  }	
  printf("%s\n",tmp);
  return 0;
}