#include <iostream>
#include <string>
using namespace std;
int main(){
  int a,b;
  while(cin >> a){
	cin >> b;
	int sum = a+b;
	string str;
	str = to_string(sum);
	cout << str.size() << endl;
  }
return 0;
}