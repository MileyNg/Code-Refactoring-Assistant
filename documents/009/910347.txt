#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int gcd = 1;
  for(int i = 2; i <= min(a,b); ++i) {
    while(a%i == 0 && b%i == 0) {
      a /= i;
      b /= i;
      gcd *= i;
    }
  }
  cout << gcd << endl;
  return 0;
}