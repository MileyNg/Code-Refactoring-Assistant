#include <stdio.h>
#include <string.h>

struct element;
typedef struct _element {
	char city;
	struct element *e[2];
}element;

int main(void) {
	char buff[105];
	int i;
	int flag;
	element *p;
	int n;
	element e[6];
	
	e[0].city = 'A';
	e[0].e[0] = (element*)&e[1];
	e[0].e[1] = (element*)&e[2];
	e[1].city = 'X';
	e[1].e[0] = NULL;
	e[1].e[1] = (element*)&e[3];
	e[2].city = 'Y';
	e[2].e[0] = (element*)&e[1];
	e[2].e[1] = NULL;
	e[3].city = 'Z';
	e[3].e[0] = (element*)&e[4];
	e[3].e[1] = (element*)&e[5];
	e[4].city = 'W';
	e[4].e[0] = (element*)&e[5];
	e[4].e[1] = (element*)&e[2];
	e[5].city = 'B';
	e[5].e[0] = (element*)&e[2];
	e[5].e[1] = (element*)&e[1];
	
	while(scanf("%s\n", buff) == 1) {
		p = &e[0];
		n = strlen(buff);
		if(buff[0] == '#') break;
		for(i=0;i<n;i++) {
			flag = 0;
			if(p->e[buff[i]-'0'] == NULL) {
				printf("No\n");
				flag = 1;
				break;
			}
			p = p->e[buff[i]-'0'];
		}
		
		if(!flag) {
			if(p!= NULL && p->city == 'B') {
				printf("Yes\n");
			} else {
				printf("No\n");
			}
		}
	}
	
	return 0;
}