#include<stdio.h>
  
int main(){
    int S[10001],T[501],U[501];
    int i,j,lengh1,lengh2,count=0,count2=0,count3,key;
     
    scanf("%d",&lengh1);
    for(i=1;i<=lengh1;i++){
        scanf("%d",&S[i]);}
      
    scanf("%d",&lengh2);
    for(i=1;i<=lengh2;i++){
        scanf("%d",&T[i]);
    }
      
    for(i=1;i<=lengh1;i++){
        for(j=1;j<=lengh2;j++){
        	if(S[i]==T[j]){	
        		U[count]=S[i];
        		count++;}
              
        }
    } 
     count3=count;
	for(i=1;i<=count3;i++){
		for(j=1;j<lengh1;j++){
			if(U[i]==S[j] && count2==1) count--;
			else if(U[i]==S[j]&&count2<1) count2++;
		}
	count2=0;}
        
    printf("%d\n",count);
      
      
    return 0;
}