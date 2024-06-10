#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

#define M 1000000
#define NIL (-1)
#define L 14

char H[M][L]; /* Hash Table */

int getChar(char ch){
	if (ch == 'A') return 1;
	else if (ch == 'C') return 2;
	else if (ch == 'G') return 3;
	else if (ch == 'T') return 4;
}

/* convert a string into an integer value */
long long getKey(char str[]){
	long long sum = 0, p = 1, i;
	for (i = 0; i < strlen(str); i++){
		sum += p*(getChar(str[i]));
		p *= 5;
	}
	return sum;
}

int h1(int key){ return key%M; }
int h2(int key){ return 1 + key % (M - 1); }

int find(char str[]){
	long long ii = getKey(str);
	int i;
	int hh1 = h1(ii);
	int hh2 = h2(ii);
	for (i = 0; i<M; i++){
		if (H[(hh1 + i*hh2) % M][0] == '\n'){}
		else if (strcmp(H[(hh1 + i*hh2) % M], str) == 0){ return 1; }
	}
	return 0;
	/* your task */
	/*
	01. i = 0
		02. repeat j = h(k, i)
		03. if T[j] == k
		04. return j
		05. else
		06. i = i + 1
		07. until T[j] == NIL or i == m
		08. return NIL
	*/
}

int insert(char str[]){
	long long ii = getKey(str);
	int hh1 = h1(ii);
	int hh2 = h2(ii);
	int i;
	for (i = 0; i<M; i++){
		if (H[(hh1 + i*hh2) % M][0]== '\0'){
			strcpy(H[(hh1 + i*hh2)%M], str);
			break;
		}
	}
	return 0;
	/* your task */
	
	/*
	int i = 0;
	do{
	  j = h(k, i)
	    if( T[j] == NIL){
	      T[j] = k;
	      return j;
	    }else{
	      int i = i + 1;
	    }
	} while (i == m);	
	*/
}

int main(){
	int i, n, h;
	char str[L], com[9];
	for (i = 0; i < M; i++) H[i][0] = '\0';

	scanf("%d", &n);

	for (i = 0; i < n; i++){
		scanf("%s %s", com, str);

		if (com[0] == 'i'){
			insert(str);
		}
		else {
			if (find(str)){
				printf("yes\n");
			}
			else {
				printf("no\n");
			}
		}
	}

	return 0;
}