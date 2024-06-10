#include <stdio.h>
int main(void){    
	int a[100];    
	int n = 0;    
	int i = 0;              
	scanf("%d",&n);    
	for(i = 0;i < n;i++){        
		scanf("%d",&a[i]);    }         
	for(i = 0;i < n;i++){        
		if(i < n -1){            
			printf("%d ",a[n-1-i]);        }else
		{            printf("%d\n",a[n-1-i]);        
			}    
	}                  
	return 0;
} 