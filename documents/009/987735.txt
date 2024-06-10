#include<stdio.h>
#define MAX 100005
#define NIL -1

typedef struct{
  int p,l,r;
}Node;
Node T[MAX];

void preorder(int);
void inorder(int);
void postorder(int);

int main(){

  int n,i,j,k,root,node,child;

  scanf("%d",&n);
 for(i = 0; i < n; i++){
    T[i].p = NIL;
    T[i].l = NIL;
    T[i].r = NIL;
 }
 for(i = 0; i < n; i++){
   scanf("%d",&node);
   for(j = 0; j < 2; j++){
     scanf("%d",&child);
     if(child != -1){
       T[child].p = node;
       if(j == 0)
	 T[node].l = child;
       else
	 T[node].r = child;
     }
   }
 } 
 for(i = 0; i < n; i++){
   if(T[i].p == NIL)
     root = i;
 }
 printf("Preorder\n");
   preorder(root);
   printf("\n");
   printf("Inorder\n");
   inorder(root);
   printf("\n");
   printf("Postorder\n");
   postorder(root);
   printf("\n");
   return 0;
}

void preorder(int root){
  printf(" %d",root);
  if(T[root].l != -1)
  preorder(T[root].l);
  if(T[root].r != -1)
    preorder(T[root].r);
}

void inorder(int root){

  if(T[root].l != -1)
    inorder(T[root].l);
  printf(" %d",root);
  if(T[root].r != -1)
    inorder(T[root].r);
}

void postorder(int root){
  if(T[root].l != -1)
    postorder(T[root].l);
  if(T[root].r != -1)
    postorder(T[root].r);
  printf(" %d",root);
}