#include<stdio.h>
#include<stdlib.h>

int main(void){
	int i = 0,stack[100],temp;
	char a;
	
	while(i != 100){
		scanf("%c",&a);
		if(a == '\n')
			break;
		if(a == '+'){
			temp = stack[i - 2] + stack[i - 1];
			stack[i - 2] = temp;
			i--;
		}
		if(a == '-'){
			temp = stack[i - 2] - stack[i - 1];
			stack[i - 2] = temp;
			i--;
		}
		if(a == '*'){
			temp = stack[i - 2] * stack[i - 1];
			stack[i - 2] = temp;
			i--;
		}
		if(a == '/'){
			temp = stack[i - 2] / stack[i - 1];
			stack[i - 2] = temp;
			i--;
		}
		if(a >= '0'&&a <= '9'){
			stack[i] = atoi(&a);
			i++;
		}
	}
	printf("%d\n",stack[0]);
	return 0;
}