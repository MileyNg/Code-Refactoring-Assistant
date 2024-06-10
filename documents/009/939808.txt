#include <stdio.h>
int main()
{
int p, a, b, x;
char op;


	while(1){
		scanf("%d %c %d", &a, &op, &b);
		if( op == '+'){
			x = a + b;
			printf("%d\n", x);
		}else if( op == '-'){
			x = a - b;
			printf("%d\n", x);
		}else if(op == '/'){
			x = a / b;
			printf("%d\n", x);
		}else if(op == '*'){
			x = a * b;
			printf("%d\n", x);
		}else if(op == '?'){
		     break;
			
		}
	}
	
	

	scanf("%d", &p);
	return 0;

}