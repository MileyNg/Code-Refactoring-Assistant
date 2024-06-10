#include <stdio.h>

#define N 10

void display(int weight, const int data[], int sw[], int n){
	
	int i;
	
	printf("wstones::%d ||", weight);
	
	for(i=0; i<n; i++){
		
		if(sw[i] == 1){
			
			printf(" %d", data[i]);
		
		}
		
	}
	
	printf("\n");
	
}

int main(void){
	
	int weight, wstones;
	const int stones[N] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512};
	int isUse[N] = {0};
	int i;
	int count;
	int lastNum;
	
	while(scanf("%d", &weight) != EOF){
		
		//printf("weight::%d\n", weight);
		
		for(i=0; i<N; i++){
			
			isUse[i] = 0;
			
		}
		
		wstones = 0;
		i = 0;
		count = 0;
		
		//分銅の重さ合計と、入力の重さが等しくなるまで繰り返す
		while(weight != wstones){
			
			//display(wstones, stones, isUse, N);
			
			//分銅の方が軽い
			if(weight > wstones){
				
				if(isUse[i] == 0){
					
					wstones += stones[i];
					isUse[i] = 1;
					
					
				}
				
				i++;
				
			}
			
			//分銅の方が重い
			else{
				
				i--;
				
				if(lastNum == i){
					
					i--;
					
				}
				
				if(isUse[i] == 1){
					
					isUse[i] = 0;
					wstones -= stones[i];
					
					lastNum = i;
					
				}
				
			}
			
		}
		
		for(i=0; i<N; i++){
			
			if(isUse[i] == 1){
				
				if(count > 0){
					
					printf(" ");
					
				}
				
				printf("%d", stones[i]);
				count++;
				
			}
			
		}
		
		printf("\n");
		
	}
	
	
	return 0;
	
}