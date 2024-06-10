#include <stdio.h>

int main(void)
{
	char str[20];
	int p,i,length,x,t;
	
	scanf("%s",str);
	
	for(i = 0;!(str[i] == 0);i++){
		length = i + 1;
		t = length;
	}
	
	for(p = 0;p < length;p++){
		
		for(i = 0;i < (t - 1);i++){
				x = str[i];
				str[i] = str[i+1];
				str[i+1] = x;
		}
		t = t - 1;
	}
	
	printf("%s\n",str);
	
	return 0;
}