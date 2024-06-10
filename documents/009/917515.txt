#include "stdio.h"
#include "string.h"

int main(){
	char str[21];
	int i=0;
	int flag=0;

	memset(str,'0',21);

	fgets(str,sizeof(str),stdin);

	for(i=20,flag=0;i>=0;i--){
		if(str[i]==0){
			flag=1;
		}else if(flag==1 && str[i]!=10){
			printf("%c",str[i]);
		}
	}

	return 0;
}