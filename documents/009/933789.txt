#include<stdio.h>
#include<string.h>

#define M (244140625/8+1)
#define NIL (-1)
#define L 14

unsigned char H[M]; /* Hash Table */

int getChar(char ch){
  if ( ch == 'A') return 1;
  else if ( ch == 'C') return 2;
  else if ( ch == 'G') return 3;
  else if ( ch == 'T') return 4;
}

/* convert a string into an integer value */
long long getKey(char str[]){
  long long sum = 0, p = 1, i;
  for ( i = 0; i < strlen(str); i++ ){
    sum += p*(getChar(str[i]));
    p *= 5;
  }
  return sum;
}

int h1(int key){ return 0/* your task */; }
int h2(int key){ return 0/* your task */; }

int find(char str[]){
	long long t = getKey(str);
	return H[t/8] & (1<<t%8);
}

int insert(char str[]){
	long long t = getKey(str);
	H[t/8] |= (1<<t%8);
}

int main(){
    int i, n, h;
    char str[L], com[9];
    for ( i = 0; i < M; i++ ) H[i] = 0;
    
    scanf("%d", &n);
    
    for ( i = 0; i < n; i++ ){
	scanf("%s %s", com, str);
	
	if ( com[0] == 'i' ){
	    insert(str);
	} else {
	    if (find(str)){
		printf("yes\n");
	    } else {
		printf("no\n");
	    }
	}
    }

    return 0;
}