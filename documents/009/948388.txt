#include<iostream>
#include<algorithm>

int calc(int a, int b){
	if (!b)return a;
	else return calc(b, a%b);
}

int main(){
	int a, b;
	std::cin >> a >> b;
	std::cout << calc(std::max(a, b), std::min(a, b)) << std::endl;
	return 0;
}