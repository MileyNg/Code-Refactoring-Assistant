#include <stdio.h>int main( void ){
   int l = 0;
while( l < 200 )    int a,b;    scanf( "%d %d",&a,&b );      a = a + b;       int n = 1;      int j = 0;      while( true ){            if( a / n >= 1 ) n *= 10;            else               break;          j++;          }      printf( "%d",j );
 l++;
 }return 0;}