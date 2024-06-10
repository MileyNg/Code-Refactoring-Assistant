#include<stdio.h>
main(){
	int a=100000,i,n; 
	
	scanf("%d",&n);
	
	for(i=0;i<n;i++){
	a=a*1.05;
	a=a+999;
	a=a/1000;
	a=a*1000;	
	}
	
	printf("%d\n",a);
	
	return 0;
}