#include <stdio.h>

void push(int v);
int pop();

int stack[1024];
int head = 0;

int main(void)
{
	int t;
	
	while (scanf("%d", &t) != EOF){
		if (t == 0){
			printf("%d\n", pop());
		}
		else {
			push(t);
		}
	}
	
	return (0);
}

void push(int v)
{
	stack[head] = v;
	head++;
}

int pop()
{
	head--;
	return (stack[head]);
}