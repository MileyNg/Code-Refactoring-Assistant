#include <stdio.h>
#include <ctype.h>

int main(){
	int i, count = 0;
	char ch, moji[1200];
	while(1){
		scanf("%c", &ch);
		if(ch == '\n') break;
		if(islower(ch)){
			moji[count] = toupper(ch);
		}else if(isupper(ch)){
			moji[count] = tolower(ch);
		} else {
			moji[count] = ch;
		}
		count++;
	}
	for(i = 0; i < count; i++){
		printf("%c", moji[i]);
	}
	printf("\n");
	return 0;
}