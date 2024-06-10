#include<stdio.h>

static const int N = 100;
void bubbleSort(int [], int);

main(){
  int i, n;
  int A[N + 1];
  scanf("%d", &n);
  
  for(i = 0; i < n; i++){
    scanf("%d", &A[i]);
  }
  bubbleSort(A, n);
  return 0;
}

void bubbleSort(int A[], int n){
  int i, j, count = 0;
  int swap;
  
  for(i = 0; i < n; i++){
    for(j = n - 1; j > i; j--){
      if (A[j] < A[j - 1]){
	swap = A[j];
	A[j] = A[j - 1];
	A[j - 1] = swap;
	count++;
      }
    }
  }
  
  for(i = 0; i < n; i++){
    printf("%d", A[i]);
    printf(" ");
  }

  printf("\n%d\n", count);
}