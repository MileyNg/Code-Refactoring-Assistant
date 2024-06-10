#include<stdio.h>
#define MAX 100005
#define NIL -1

/*
 p: parent
 l: left-child
 r: right sibling
 */
struct Node{
  int p, l, r;
};
struct Node T[MAX]; // Tree
int n;
void preorder(int u){
  printf(" %d",u);
  if(T[u].l!=NIL) preorder(T[u].l);
  if(T[u].r!=NIL) preorder(T[u].r);
}

void inorder(int u){
    if (T[u].l!=NIL) inorder(T[u].l);
    printf(" %d",u);
    if (T[u].r!=NIL) inorder(T[u].r);
}

void postorder(int u){
    if (T[u].l!=NIL) postorder(T[u].l);
    if (T[u].r!=NIL) postorder(T[u].r);
    printf(" %d",u);
}

void print(int u){
  printf("Preorder\n");
  preorder(u);
  printf("\n");
  printf("Inorder\n");
  inorder(u);
  printf("\n");
  printf("Postorder\n");
  postorder(u);
  printf("\n");
}

int main(){
  int i, j, d, v, c, l,tmp;
  
  scanf("%d", &n);
  
  for ( i = 0; i < n; i++ ) {
    T[i].p = T[i].l = T[i].r = NIL;
  }
  
  for ( i = 0; i < n; i++ ){
    scanf("%d %d %d", &v, &d, &c);
    T[v].l = d;
    T[v].r = c;
    T[d].p = T[c].p = v;
  }
  for ( i = 0; i < n; i++ ){
    if(T[i].p==NIL) print(i);
  }
  return 0;
}