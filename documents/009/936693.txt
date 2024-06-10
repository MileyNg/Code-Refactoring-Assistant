#include <iostream>
using namespace std ;

int main (){

  int a[101] , i = 0 , n = 0 , num = 0 ;

  cin >> n ;

  for ( i = 1 ; i <= n ; i++ ){

    cin >> num ;

    a[i] = num ;
}
  cout << a[n];
  for ( i = n - 1 ; i >= 1 ; i-- ){
    
    cout << ' ' << a[i] ;
    //   if (i){
    // cout << " " ;
    
    }    
  
  cout << "\n" ;

  return 0 ;

}