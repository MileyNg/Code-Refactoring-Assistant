#include <stdio.h>

#define MAX_N 1000000

int isPrime[ MAX_N + 1 ] = { 0, 0, 1 }, num_p[ MAX_N + 1 ] = {};

int main( void ) {
    int i, j, n;

    for ( i = 3; i <= MAX_N; i += 2 )
        isPrime[ i ] = 1;

    for ( i = 3; i * i <= MAX_N; i += 2 )
        if ( isPrime[ i ] )
            for ( j = i * 2; j <= MAX_N; j += i )
                isPrime[ j ] = 0;

    for ( i = 1; i <= MAX_N; i++ )
        num_p[ i ] = num_p[ i - 1 ] + isPrime[ i ];

    for ( ; scanf( "%d", &n ) == 1; printf( "%d\n", num_p[ n ] ) ) ;

    return 0;
}