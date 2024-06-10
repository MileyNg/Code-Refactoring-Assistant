#include <stdio.h>
int main(){
	int n[500],x[500], a=0, b=0, c=0, d=0, f=0;
	int  e[500]={0};
	for(d=0;;d++){
		scanf("%d %d", &n[d], &x[d]);
		if(n[d] == 0 && x[d] == 0)break;
		for(a = 1; a <= n[d]; a++){
			for(b = 1; b <= n[d]; b++){if(b == a)break;
				for(c = 1; c <= n[d]; c++){if( c == a || c == b )break;
				if(a+b+c==x[d]){e[d]++;}
				}
			}
		}
	}
for(f = 0; f < d; f++){
	printf("%d\n", e[f]);
}

	
	

	return 0;
}