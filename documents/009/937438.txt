#include <stdio.h>

int stack[1024];
int head = 0;
void push(int v)
{
	stack[head] = v;
	head++;
}
int pop()
{
	int v;
	v = stack[head - 1];
	head--;
	return (v);
}

int main(void)
{
	int train;
	while (~scanf("%d", &train)){
		if (train == 0){
			printf("%d\n", pop());
		}
		else {
			push(train);
		}
	}
	return (0);
}