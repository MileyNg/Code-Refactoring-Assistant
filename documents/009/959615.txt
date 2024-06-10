#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  int n,m,min,max,i,ans;

  cin >> n >> m;
  if(n < m) { 
    min = n;
    max = m;
  }
  else {
    min = m;
    max = n;
  }
  for(i=1; i<min/2; i++){
    if(min%i==0 && max%i==0) ans = i;
  }
  if(max%min==0) ans=n;
  cout<<ans<<endl;
  return 0;
}