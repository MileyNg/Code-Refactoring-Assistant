#include<stdio.h>
#define MAX 100005
#define NIL -1

struct Node{ int p, l, r, dg,d, s, h;};
struct Node T[MAX]; // Tree

int count1 = 0, n;
int getdepth(int);
int prinr(int);
int getheight(int, int);
void walk(int);
void walk1(int);
void walk2(int);

int getdepth(int d){

  if(d == NIL){
    return count1;
  }

  else{
    count1++;
    return getdepth(T[d].p);
  }

}

int getheight(int h, int c){

  int a=0, b=0;
  
  if(T[h].r != NIL){
    a = getheight(T[h].r, c+1);
  }
  
  if(T[h].l != NIL){
    b = getheight(T[h].l, c+1);
  } 
  
  if(T[h].l == NIL && T[h].r == NIL){
    return c;
  }
  
  if(a>=b){
    return a;
  }
  return b;
  
}
  

void print(key){
  int i;
 
  printf("Preorder\n");
  walk(key);

  printf("\n");

  printf("Inorder\n");
  walk1(key);

  printf("\nPostorder\n");
  walk2(key);

  printf("\n");

}

void walk(int v){

  printf(" %d", v);
  if(T[v].l!=NIL){
    walk(T[v].l);
  }
  if(T[v].r!=NIL){
    walk(T[v].r);
  }

}

void walk1(int v){

  if(T[v].l!=NIL){
    walk1(T[v].l);
    printf(" %d", v);
  }
  else{
    printf(" %d", v);
  }

  if(T[v].r!=NIL){
    walk1(T[v].r);
  }
}

void walk2(int v){

  if(T[v].l!=NIL){
    walk2(T[v].l);

  }
  if(T[v].r!=NIL){
    walk2(T[v].r);

  }

  printf(" %d", v);

}

int prinr(int u){

  if(T[u].p == NIL){
    return 1;
  }
  
  else{
    return 0;
  }

}

main(){
  int i, j, d, v, c, l, r, key;

  scanf("%d", &n);

  for ( i = 0; i < n; i++ ) {
    T[i].p = T[i].l = T[i].r = T[i].dg = T[i].s = NIL;
  }

  for ( i = 0; i < n; i++ ){
    c=0;
    scanf("%d %d %d", &v, &l, &r);

    T[v].l = l;
    T[v].r = r;

    T[l].p = v;
    T[l].s = r;

    T[r].p = v;
    T[r].s = l;

    if(l == NIL){
      c++;
    } 
    if(r == NIL){
      c++;
    }

    if(c == 0){
      T[v].dg = 2;
    }
    else if(c == 1){
      T[v].dg = 1;
    }
    else{
      T[v].dg = 0;
    }

  }
 

  for(i=0; i<n; i++){
    count1 = 0;

    T[i].d  = getdepth(T[i].p);
    T[i].h = getheight(i, 0);

  }

  for(i=0; i<n; i++){
    if(prinr(i)==1){
      key = i;
      break;
    }
  }


  print(key);
  return 0;
}