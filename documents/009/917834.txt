#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ll a,b,sum,z;
    while(cin>>a>>b)
    {
        sum=a+b;
        z=floor(log10(sum))+1;
        cout<<(ll)z<<endl;
    }
    return 0;
}