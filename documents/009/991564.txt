#include<stdio.h>
int main(){
	
	int a, i[100]={}, b, c;
	char mozi[1001]={};
	for(a=0;a<1000;a++){
	scanf("%s", mozi);
		if(mozi[0]=='0'){break;}
		for(b=0;b<1000;b++){
			
			i[a]+=mozi[b]-'0';
			if(mozi[b+1]=='\0')break;
			
		}
	}
	for(c=0;c<a;c++){
		printf("%d\n",i[c]);
	}
	return 0;
}