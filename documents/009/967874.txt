#include<iostream>
using namespace std;

int main(){
  
  int n,i,j,s;
  
  cin >>n ;
 
  int num[n];
 
  for(s = 0;s < n;s++){
  cin >>num[s] ;
  }

  for( i = n-1; i>0;i--){
    cout <<num[i] <<" " ;
    
  }
  cout <<num[0] <<"\n" ;
  
  return 0;
}