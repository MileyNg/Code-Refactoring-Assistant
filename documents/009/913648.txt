#include <stdio.h>
 int main( void ){
    int a,b;
    scanf( "%d %d",&a,&b );
    a = a + b;
     int n = 1;
    int j = 0;
    while( true ){
        if( a / n >= 1 ) n = n * 10;
        else               break;
        j++;
    }
    printf( "%d",j );
    return 0;
}