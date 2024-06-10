#include<stdio.h>//ラウンドロビンスケジューリング

typedef struct process{
	char name[10];
	int time;
}PROC;

PROC list[100000];

int main(void){
	int i,n,quan,total=0,max=0,mnum;
	
	scanf("%d %d",&n,&quan);

	for(i = 0;i < n;i++){
		scanf("%s %d",list[i].name,&list[i].time);
	}
	for(i = 0;i < n;i++){
		if(list[i].time >= max){
			max = list[i].time;
			mnum = i;
		}
	}

	for(i = 0;;i++){
		if(i == n){
			i = 0;
		}
		if(list[i].time <= quan && list[i].time != 0){
			total += list[i].time;
			list[i].time = 0;
			printf("%s %d\n",list[i].name,total);
			if(list[mnum].time == 0){
				break;
			}
		}else if(list[i].time > quan){
			list[i].time -= quan;
			total += quan;
		}
	}
	

	return 0;
}