#include<stdio.h>

int main(void)
{
  int count[100];
  int i, j, k, l, soeji = 0;
  int num;

  while(scanf("%d",&num) != EOF){
    count[soeji] = 0;

    for(i=0; i<=9; i++){
      for(j=0; j<=9; j++){
	for(k=0; k<=9; k++){
	  for(l=0; l<=9; l++){
	    if(num == i+j+k+l){
	      count[soeji]++;
	    }
	  }
	}
      }
    }
  soeji++;
  }
  for(i=0; i<soeji; i++){
  printf("%d\n", count[i]);
  }

  return 0;
}