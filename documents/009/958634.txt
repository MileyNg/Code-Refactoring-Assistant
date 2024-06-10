#include<stdio.h>
int main(){
	int i=0,j=0,n,l;
	int a[10],b[10];
	do{
		scanf("%d",&n);
		if(n==0){
			i--;
			b[j]=a[i];
			j++;
		}
		else{a[i]=n;
			i++;
		}
	}while(i!=0);
	for(l=0;l<j;l++){
		printf("%d\n",b[l]);
	}
	return 0;
}