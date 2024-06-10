#include <stdio.h>
void calc(int a,int b, char op){
	int ans;
	switch (op) {
	case '+':ans = a + b;
		break;
	case '-':ans = a - b;
		break; 
	case '*':ans = a * b;
		break; 
	case '/':ans = a / b;
		break;
	}
	printf("%d\n", ans);
}
int main(void){
	int a, b, ans;
	char op;
	while (1){
		scanf("%d %c %d", &a, &op, &b);
		if (op == '?')break;
		calc(a, b, op);
	}
	return 0;
}