#include <stdio.h>

int main(void) {
  int a, b, result;
  char op;

  for (; scanf("%d %c %d", &a, &op, &b), op != '?'; ) {
    switch (op) {
      case '+': result = a + b; break;
      case '-': result = a - b; break;
      case '*': result = a * b; break;
      case '/': result = a / b; break;
    }

    printf("%d\n", result);
  }

  return 0;
}