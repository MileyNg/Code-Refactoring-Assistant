#include<stdio.h>
#include<string.h>
#define M 100000
typedef struct DIC{
  char coma[10];
  char key[12];
  int c;
}D;

D D1[M],D2[M],D3[M],D4[M],D5[M],D6[M],D7[M],D8[M],D9[M],D10[M],D11[M];
static int t1=0,t2=0,t3=0,t4=0,t5=0,t6=0,t7=0,t8=0,t9=0,t10=0,t11=0;
unsigned hash(char *v){
  int h;
  for(h=0;*v!='\0';v++)
    h=(64*h + *v)%11;
  return h; 
}

void insert(D d){
  if(hash(d.key)==0){
    strcpy(D1[t1].key,d.key);
    t1++;
  }
  else if(hash(d.key)==1){
    strcpy(D2[t2].key,d.key);
    t2++;
  }
  else if(hash(d.key)==2){
    strcpy(D3[t3].key,d.key);
    t3++;
  }
  else if(hash(d.key)==3){
    strcpy(D4[t4].key,d.key);
    t4++;
  }
  else if(hash(d.key)==4){
    strcpy(D5[t5].key,d.key);
    t5++;
  }
  else if(hash(d.key)==5){
    strcpy(D6[t6].key,d.key);
    t6++;
  }
  else if(hash(d.key)==6){
    strcpy(D7[t7].key,d.key);
    t7++;
  }
  else if(hash(d.key)==7){
    strcpy(D8[t8].key,d.key);
    t8++;
  }
  else if(hash(d.key)==8){
    strcpy(D9[t9].key,d.key);
    t9++;
  }
  else if(hash(d.key)==9){
    strcpy(D10[t10].key,d.key);
    t10++;
  }
  else{
    strcpy(D11[t11].key,d.key);
    t11++;
  }
}

int search(D d){
  int i;
  if(hash(d.key)==0){
    for(i=0;i<t1;i++){
      if(strcmp(D1[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else if(hash(d.key)==1){
    for(i=0;i<t2;i++){ 
      if(strcmp(D2[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else if(hash(d.key)==2){
    for(i=0;i<t3;i++){ 
      if(strcmp(D3[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else if(hash(d.key)==3){
    for(i=0;i<t4;i++){ 
      if(strcmp(D4[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else if(hash(d.key)==4){
    for(i=0;i<t5;i++){ 
      if(strcmp(D5[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else if(hash(d.key)==5){
    for(i=0;i<t6;i++){ 
      if(strcmp(D6[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else if(hash(d.key)==6){
    for(i=0;i<t7;i++){ 
      if(strcmp(D7[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else if(hash(d.key)==7){
    for(i=0;i<t8;i++){ 
      if(strcmp(D8[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else if(hash(d.key)==8){
    for(i=0;i<t9;i++){ 
      if(strcmp(D9[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else if(hash(d.key)==9){
    for(i=0;i<t10;i++){ 
      if(strcmp(D10[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
  else{
    for(i=0;i<t11;i++){ 
      if(strcmp(D11[i].key,d.key)==0)
	return 0;
    }
    return 1;
  }
}
main(){
  D Dic[M];
  int n,i;
  
  scanf("%d",&n);
  for(i=0;i<n;i++)
    scanf("%s %s",Dic[i].coma,Dic[i].key);
  for(i=0;i<n;i++)
    if(Dic[i].coma[0]=='i')
      insert(Dic[i]);
    else
      if(search(Dic[i])==0)
	printf("yes\n");
      else
	printf("no\n");
  return 0;
}