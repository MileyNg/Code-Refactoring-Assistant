#include <iostream>
using namespace std;

int main()
{
  int a,b,sum,digit;
  while(cin << a << b){
    digit = 0;
    sum = a + b;
    while(sum > 0){
      sum /= 10;
      digit += 1;
    }
    cout << digit << endl;
  }
}