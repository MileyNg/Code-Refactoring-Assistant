#include<stdio.h>
#define MAX 100005
#define NIL -1
int n;
struct Node{
  int p; //parent
  int l; //left-child
  int r; //right sibiling
};
struct Node T[MAX];
void preorder(int i){
  printf(" %d", i);
  if(T[i].l!=NIL) preorder(T[i].l);
  if(T[i].r!=NIL) preorder(T[i].r);
}
void inorder(int i){
  if(T[i].l!=NIL) inorder(T[i].l);
  printf(" %d",i);
  if(T[i].r!=NIL) inorder(T[i].r);
}
void postorder(int i){
  if(T[i].l!=NIL) postorder(T[i].l);
  if(T[i].r!=NIL) postorder(T[i].r);
  printf(" %d",i);
}
int main(void){
  int i;
  int d;
  scanf("%d", &n);
  for ( i=0; i<n; i++ ) T[i].p=T[i].l=T[i].r=NIL;
  for ( i=0; i<n; i++ ){
    scanf("%d", &d);
    scanf("%d %d", &T[d].l, &T[d].r);
    T[T[d].l].p=T[T[d].r].p=d;
  }
  for ( i=0; i<n; i++ ) if(T[i].p==NIL) break;
  printf("Preorder\n");
  preorder(i);
  printf("\nInorder\n");
  inorder(i);
  printf("\nPostorder\n");
  postorder(i);
  printf("\n");
  return 0;
}