#include<stdio.h>
#include<string.h>

#define M 1000000
#define L 14

char H[M][L]; /* Hash Table */

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

int h1(int key){ 
  int h;
  h =  key % M; 
  return h; 
}
int h2(int key){
  int h;
  h = 1 + key % (M-1);
  return h;
}

int find(char str[]){
  int i=0,j=0;
  int a=0,b=0,key=0;
  key=getKey(str);
  a = h1(key);
  b = h2(key);
  for(i=a;j<M;i+=b)
    {
      if(i >= M) 
         i = i % M;
      if(strcmp(H[i],"")==0) 
         return 0;
      else if(strcmp(H[i],str)== 0)
         return 1;
      j++;
    }
  return 0;


}

int insert(char str[]){
  int i=0,j=0;
  int a=0,b=0,key=0;
  key = getKey(str);
  a = h1(key);
  b = h2(key);
 
  for(i=a;j<M;i+=b)
    {
    if(i>=M) 
      i = i % M;
    if(strcmp(H[i],"")==0)
     {
      strcpy(H[i],str);
      return 1;
      }
    j++;
    }
  return 0;

}

int main(){
    int i, n, h;
    char com[9],str[L];
    for ( i = 0; i < M; i++ ) 
      H[i][0] = '\0';
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