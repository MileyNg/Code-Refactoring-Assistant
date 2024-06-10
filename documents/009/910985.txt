#include<stdio.h>

int main(void){
	int i,j,temp,rtime,tri[3];

	scanf("%d",&rtime);
	
	for(i = 0;i < rtime;i ++){
		for(j = 0;j < 3;j ++){
			scanf("%d",&tri[j]);
		}
		for(j = 0;j < 3;j ++){
			temp = tri[0] * tri[0];
			if(temp == tri[1] *tri[1] + tri[2] * tri[2]){
				printf("YES\n");
				break;
			}
			if(j == 2){
				printf("NO\n");
			}
			temp = tri[2];
			tri[2] = tri[1];
			tri[1] = tri[0];
			tri[0] = temp;
		}
	}
	return 0;
}