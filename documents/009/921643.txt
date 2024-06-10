#include<iostream>
#include<cstdlib>
using namespace std;

// a > b
int gcd(int a, int b)
{
        int r;
        while(1){
                r = a%b;
                if( !r ){ return b; }
                else{ a = b; b = r; }
        } 
}


int main()
{
        int a, b;
        cin >> a >> b;
        cout << gcd(a, b) << endl;
        return 0;
}