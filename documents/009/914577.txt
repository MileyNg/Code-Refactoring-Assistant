#include<stdio.h>

int main(int argc,char* argv[]){

  int i,val,time,count = 0;
  //累積時間
  int sytime = 0;
  int dat[100000];
  char sdat[100000][11];

  scanf("%d %d",&val,&time);

  for(i = 0;i < val;i++)
    scanf("%s %d",sdat[i],&dat[i]);

  while(count < val){
    for(i = 0;i < val;i++){
      if(dat[i]!= -1){
	if((dat[i] = dat[i] - time )<= 0){
	  sytime = sytime + time + dat[i];
	  printf("%s %d\n",sdat[i],sytime);
	  dat[i] = -1;
	  count++;
	}
	else sytime += time;
      }
    }
  }
  return 0;
}