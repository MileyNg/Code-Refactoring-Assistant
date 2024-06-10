#include<iostream>

int getDigit(int x);

int main(){
	int a, b;
	
	while(std::cin >> a >> b){
		int n = a + b;
		std::cout << getDigit(n) << std::endl;
	}
	
	return 0;
}


int getDigit(int x){
	int digit = 0;
	
	while(x >= 1){
		x /= 10;
		++digit;
	}
	
	return digit;
}