/*
ハッシュ(オープンアドレス法、ダブルハッシシング)
A=2,C=3,G=4,T=5
*/

#define M 5000000

#include<stdio.h>
#include<string.h>

void insert(char*);
int find(char*);
int get_hash_num(char*);
int get_keycode(char);

typedef struct{
  int num;
  char name[13];
}hash_struct;

//numの部分を0で初期化
hash_struct hash[M]={0};

int main(void){
  int n;
  int i;
  char str[13],input[7];

  scanf("%d",&n);

  for(i=0;i<n;i++){
    scanf("%s %s",input,str);

    if(input[0]=='i') insert(str);

    if(input[0]=='f'){
      if(find(str)==1) printf("yes\n");
      else printf("no\n");
    }
  }

  return 0;
}

void insert(char *str){
  int i=0,hash_num,data;

  data=get_hash_num(str);

  while(1){
    hash_num=((data%M)+i*(data%(M-1)+1))%M;
    if(hash[hash_num].num==0){
      hash[hash_num].num=data;
      strcpy(hash[hash_num].name,str);
      break;
    }
    i++;
  }
}

int find(char *str){
  int data,hash_num,i=0;

  data=get_hash_num(str);
 
  while(1){
    hash_num=((data%M)+i*(data%(M-1)+1))%M;
    if(hash[hash_num].num==0) return 0;
    if(strcmp(hash[hash_num].name,str)==0) return 1;
    i++;
  }
}

int get_hash_num(char *str){
  int data=1,cnt=0;

  while(str[cnt]!='\0'){
    data*=get_keycode(str[cnt]);
    cnt++;
  }

  return data;
}

int get_keycode(char work){
  switch(work){
  case 'A':
    return 2;
  case 'C':
    return 3;
  case 'G':
    return 4;
  case 'T':
    return 5;
  }
}