#include<stdio.h>
#include<string.h>

#define Len 14
#define N 999997

char H[N][Len]; 

int getChar(char ch){
  if ( ch == 'A') return 1;
  else if ( ch == 'C') return 2;
  else if ( ch == 'G') return 3;
  else if ( ch == 'T') return 4;
}


long long getKey(char str[]){
  long long sum = 0, p = 1, i;
  for ( i = 0; i < strlen(str); i++ ){
    sum += p*(getChar(str[i]));
    p *= 5;
  }
  return sum;
}

int h1(int key){ return key%N; }
int h2(int key){ return 1+(key%(N-1)); }

int find(char str[]){
  int a=0,k=0;
  long long sum;
  sum=getKey(str);

  while(1){
    k=(h1(sum)+a*h2(sum))%N;
    if(H[k][0]=='\0' || a==N){
      return 0;
    }
    if(strcmp(H[k],str)==0){
      return 1;
    }
    else a++;
  }

}

void insert (char str[]){
  int b=0,k=0;
  long long sum;
  sum=getKey(str);
  while(b!=N){
    k=(h1(sum)+b*h2(sum))%N;
    if(H[k][0]=='\0'){
      strcpy(H[k],str);
      break;
    }
    else b++;
    
  }
}



int main(){
    int i, n, h;
    char str[Len], com[9];
    for ( i = 0; i < N; i++ ) H[i][0] = '\0';
    
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