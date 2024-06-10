#include <iostream>
using namespace std;

int main()
{
  int a,b,sum,digit=0;
  try{
    while(1){
      digit = 0;
      cin >> a >> b;
      sum = a + b;
      while(sum > 0){
	sum /= 10;
	digit++;
      }
      cout << digit;
    }
  }catch(...){
    return 0;
  }
}