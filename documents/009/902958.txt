#include <stdio.h>
#define CARD 4
#define NUM 13
int cvt_char_to_num(char);
char cvt_num_to_char(int);
void Card();
void outputCard(int [4][13]);

int cvt_char_to_num(char card){
	switch (card){
	case'S':return 0;
	case'H':return 1;
	case'C':return 2;
	case'D':return 3;
	default:return -1;
	}
}
char cvt_num_to_char(int card){
	switch (card){
	case 0:return 'S';
	case 1:return 'H';
	case 2:return 'C';
	case 3:return 'D';
	default:return -1;
	}
}
void Card(){
	int card[4][13] = {0};
	int max_num, card_num;
	char card_char;
	scanf("%d", &max_num);
	while (max_num--){
		scanf(" %c %d", &card_char, &card_num);
		card[cvt_char_to_num(card_char)][--card_num] = 1;
	}
	outputCard(card);
}
void outputCard(int card[4][13]){
	int i, j;
	for (i = 0; i < CARD; i++){
		for (j = 0; j < NUM; j++){
			if (!card[i][j])printf("%c %d\n", cvt_num_to_char(i),j+1);
		}
	}
}

int main(void){
	Card();
	return 0;
}