#include <stdio.h>
#define N 100005
#define NIL -1

struct Node{
  int p, left, right;
};
struct Node T[N];
int n;

void inorder(int p){
  if(p != NIL) {
    inorder(T[p].left);
    printf(" %d", p);
    inorder(T[p].right);
  }
}

void postorder(int p){
if(p != NIL) {
    postorder(T[p].left);
    postorder(T[p].right);
    printf(" %d", p);
  }
}

void preorder(int p){
if(p != NIL) {
  printf(" %d", p);
  preorder(T[p].left);
  preorder(T[p].right);
  }
}



main(){
  int i, id;

  scanf("%d", &n);
  for(i = 0; i < n; i++){
    T[i].left = T[i].p = T[i].right = NIL;
  }
  for(i = 0; i < n; i++){
    scanf("%d", &id);
    scanf("%d %d", &T[id].left, &T[id].right);
      T[T[id].left].p = id;
      T[T[id].right].p = id;
    }    

  printf("Preorder\n");
  for(i = 0; i < n; i++){
    if(T[i].p == NIL){
      preorder(i);
    }
  }
  printf("\nInorder\n");
  for(i = 0; i < n; i++){
    if(T[i].p == NIL){
      inorder(i);
    }
  }
  printf("\nPostorder\n");
  for(i = 0; i < n; i++){
    if(T[i].p == NIL){
      postorder(i);
    }
  }
  printf("\n");
  return 0;
}