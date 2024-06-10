#include<stdio.h>
int main(){
	int i=0,j=0,n,l;
	int a[10],b[10];
	while(scanf("%d",&n)!=EOF){
		if(n==0){
			i--;
			b[j]=a[i];
		    printf("%d\n",b[j]);
			j++;
		}
		else{
		    a[i]=n;
			i++;
		}
	}
	return 0;
}