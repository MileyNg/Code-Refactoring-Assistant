#include <stdio.h>

typedef struct{
  int id,l,r;
} Node;

int n;
Node t[25];

int search(int x){
  int i;
  for(i=0;i<n;i++){
    if(t[i].id==x)return i;
  }
}

int search2(int x){
  int i;
  for(i=0;i<n;i++){
    if(t[i].l==x||t[i].r==x)return i;
  }
  return -1;
}

void pre(int x){
  printf(" %d",t[x].id);
  if(t[x].l!=-1)pre(search(t[x].l));
  if(t[x].r!=-1)pre(search(t[x].r));
}

void in(int x){
  if(t[x].l!=-1)in(search(t[x].l));
  printf(" %d",t[x].id);
  if(t[x].r!=-1)in(search(t[x].r));
}

void post(int x){
  if(t[x].l!=-1)post(search(t[x].l));
  if(t[x].r!=-1)post(search(t[x].r));
  printf(" %d",t[x].id);
}

int getroot(int x){
  if(search2(x)==-1)return x;
  return getroot(search2(x));
}

int main(){
  int i;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d %d %d",&t[i].id,&t[i].l,&t[i].r);
  }
  int ro = search( getroot(t[0].id) );
  printf("Preorder\n");
  pre(ro);
  printf("\nInorder\n");
  in(ro);
  printf("\nPostorder\n");
  post(ro);
  printf("\n");
  return 0;
}