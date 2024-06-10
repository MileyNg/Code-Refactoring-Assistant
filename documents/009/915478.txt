#include <stdio.h>

int main(){
	int a;
	int b;
	int c;
	scanf("%d %d %d",&a,&b,&c);
	if (a<b && a<c && b<c){
		printf("Yes\n");}
	if (a>b){
	printf("No\n");}else if(b>c){
		printf("No\n");}else if(a>c){
		printf("No\n");}
	return 0;
}