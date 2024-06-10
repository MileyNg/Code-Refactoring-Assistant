#include<iostream>
using namespace std;

int main(void){

int n ;
int ar[100] ;

cin >> n ;


for(int i=0;i<n;i++){
cin >> ar[i] ;
}

for(int k=1;k<n;k++){
cout << ar[n-k] << "\n" ;
}

return 0 ;

}