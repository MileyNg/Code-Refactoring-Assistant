#include<stdio.h>
void change(int *, int *);
int main(){
  int a, b, c, n;
  scanf("%d", &n);

  for(; n > 0; n--){
    scanf("%d %d %d", &a, &b, &c);
    change(&a, &c);
    change(&b, &c);
    if(a * a + b * b == c * c){
      printf("YES\n");
    }else{
      printf("NO\n");
    }
  }
  return 0;
}

void change(int *x, int *y){
  int tmp;
  if(*x > *y){
    tmp = *x;
    *x = *y;
    *y = tmp;
  }
}