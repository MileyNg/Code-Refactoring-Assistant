#include <stdio.h>
#include <string.h>

int check(char c)
{
	if (c == ',' || c == '.' || c == ' ' || c == '\n' || c == 0){
		return 0;
	}
	else {
		return 1;
	}
}

int main(void)
{
	char str[1026];
	int i;
	int len;
	char word[128];
	char flag = 0;
	
	fgets(str, 1025, stdin);
	for (i = 0; check(str[i]) == 1; i++){
		word[i] = str[i];
	}
	word[i] = 0;
	len = strlen(word);
	if (3 <= len && len <= 6){
		printf("%s", word);
		flag = 1;
	}
	for (; str[i] != 0;){
		int j;
		
		for (j = 0; check(str[i]) == 1; i++, j++){
			word[j] = str[i];
		}
		word[j] = 0;
		len = strlen(word);
		if (3 <= len && len <= 6){
			if (flag == 0){
				printf("%s", word);
				flag = 1;
			}
			else {
				printf(" %s", word);
			}
		}
		while (str[i] != 0 && check(str[i]) == 0){
			i++;
		}
	}
	puts("");
	
	return 0;
}