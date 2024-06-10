#include<stdio.h>
main(){
	unsigned int a,b,n,m,c,tmp;
	
	double n1,n2;
	
	while(1){
		if(scanf("%d %d",&a,&b) == EOF) break;
		
		//最大公約数 (n)
		n=a; m=b;
		if(a<b){ n=b; m=a; }
		
		while(m != 0){
			tmp=n%m;
			n=m;
			m=tmp;
		}
		
		//最小公倍数 (c)
		
		c = (a/n) * b;
		
		printf("%d %d\n",n,c);
	}
	
	return 0;
}