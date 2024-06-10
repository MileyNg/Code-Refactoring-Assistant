#include <stdio.h>
#include <memory.h>
#define S 0
#define H 1
#define C 2
#define D 3

int main(void) {
	int i, j, size, num;
	char c;
	char FIG[] = {'S', 'H', 'C', 'D'};
	int card[4];
	memset((char*)card, 0x00, sizeof(card));
	
	scanf("%d\n", &size);
	for(i=0;i<size;i++) {
		scanf("%c %d\n", &c, &num);
		switch(c) {
			case 'S':
				card[S] |= 1 << num;
			break;
			case 'H':
				card[H] |= 1 << num;
			break;
			case 'C':
				card[C] |= 1 << num;
			break;
			case 'D':
				card[D] |= 1 << num;
			break;
		}
	}
	
	for(i=0;i<4;i++) {
		for(j=1;j<=13;j++) {
			if((card[i] & (1 << j)) == 0) {
				printf("%c %d\n", FIG[i], j);
			}
		}
	}

	return 0;
}