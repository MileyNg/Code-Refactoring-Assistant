#include<stdio.h>
main(){
	int i,j,n,a[5000];
	
	int sum = 0,max = 0,ans = 0;
	
	
	while(1){
		
		max = 0;
	
		scanf("%d",&n);
		
		if(n==0) break;
		
		for(i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		
		//後ろの負数をカット
		
		for(i = n - 1; (i >= 0)&&(a[i] <= 0); i--);
		
		n = i;
		
		//頭の負数をカット
		
		for(i = 0; a[i] <= 0; i++);
		
		//printf("i = %d\n",i);
		
		//最後の整数までループ
		
		for( ;i <= n; i++){
			
			sum = 0;
			
			for(j = i; j <= n; j++) sum += a[j];
			
			max = sum;
			
			for(j = n; j >= i; j--){
				
				sum -= a[j];
				
				if(sum > max) max = sum;
				
			}
			
			if(max > ans ) ans = max;
		}
		
		//printf("n = %d\n",n);
		
		printf("%d\n",ans);
		
		
		sum = 0;
		max = 0;
		ans = 0;
		
	}

	return 0;
}