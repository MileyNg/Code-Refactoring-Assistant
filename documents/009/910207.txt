#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  if(max(a,b) % min(a,b) == 0) {
    cout << min(a,b) << endl;
    return 0;
  }
  for(int i = min(a,b)/2; i >= 1; --i) {
    if(a % i == 0 && b % i == 0) {
      cout << i << endl;
      return 0;
    }
  }
  return 0;
}