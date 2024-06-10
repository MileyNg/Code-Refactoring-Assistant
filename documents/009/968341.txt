//Using Stack Data Structure

#include <stdio.h>

int stack[10];
int n;	//stack pointer

void init(){
	n = 0;
}

void push(int x){
	stack[n++] = x;
}

int pop(){
	return stack[--n];
}

int main(void){
	init();
	int o;
	while(scanf("%d", &o) != EOF){
		if(o == 0){
			printf("%d\n", pop());
		}else{
			push(o);
		}
	}
	
	return 0;
}