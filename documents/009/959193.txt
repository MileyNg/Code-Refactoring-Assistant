#include <iostream>
#include <cstdio>
using namespace std;

int main(){
  double x, s, d;
  double pai = 3.141592653589;

  cin >> x;

  s = pai * x * x;
  d = 2 * pai * x;
  printf("%.5lf %.5lf\n", s, d);

  return 0;
}