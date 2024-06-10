#include<stdio.h>
#include<stdlib.h>
#include<string.h>

main(){
  int x[100],y[100],i=0,k=0,j=0,tasu=0,hiku=0,kakeru=1,l;
  char s[101];

  while( scanf("%s",s) != EOF ){


    if ( s[0] == '+' ){
      y[k-2]=y[k-1]+y[k-2];
      k=k-2;
      k=k+1;
      //printf("%d\n",y[k-2]);
    } 
    else if ( s[0] == '-' ){
      y[k-2]=y[k-2]-y[k-1];
      k=k-2;
      k=k+1;
    }
    else if ( s[0] == '*' ){
      y[k-2]=y[k-2]*y[k-1];
      k=k-2;
      k=k+1;
    }
    else {
      y[k] = atoi(s);
      k=k+1;
      //  printf("%d  %d\n",y[k-1],k);
  }
    i=i+1;
    //printf("%d",i);
  }
  printf("%d\n",y[k-1]);
 
  return 0;
}