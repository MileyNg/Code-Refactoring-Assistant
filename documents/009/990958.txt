#include<stdio.h>
#include<stdlib.h>
#define NIL NULL

struct node{
  struct node *l;
  struct node *r;
  struct node *p;
  int key;
};

typedef struct node *Node;

Node root;
Node TreeMin(Node x){
}

Node TreeSearch(Node x, int k){
  if(x==NIL||k==x->key) return x;
  if(k<x->key) return TreeSearch(x->l,k);
  else return TreeSearch(x->r,k);
}

Node TreeSuccessor(Node x){
}

void TreeDelete(Node z){
  Node y; // node to be deleted
  Node x; // child of y
}

void TreeInsert(int k){
  Node y=NIL;
  Node x=root;
  Node z;
  z=malloc(sizeof(struct node));
  z->key=k;
  z->l=NIL;
  z->r=NIL;

  while(x!=NIL){
    y=x;
    if(z->key<x->key) x=x->l;
    else x=x->r;
  }
  z->p=y;
  if(y==NIL) root=z;
  else if(z->key<y->key) y->l=z;
  else y->r=z;
}

void Iorder(Node u){ //Inorder
  if(u!=NIL){
      Iorder(u->l);
      printf(" %d",u->key);
      Iorder(u->r);
  }
}

void Porder(Node u){ //Preorder
  printf(" %d",u->key);
  if(u!=NIL){
    if(u->l!=NIL)Porder(u->l);
    if(u->r!=NIL)Porder(u->r);
  }
}

int main(){
  int n,i,x;
  char array[20];
  scanf("%d",&n);

  for(i=0;i<n;i++){
    scanf("%s",array);
    if(array[0]=='f'){
      scanf("%d",&x);
      Node t = TreeSearch(root,x);
      if(t!=NIL) printf("yes\n");
      else printf("no\n");
    } else if(array[0]=='i'){
      scanf("%d",&x);
      TreeInsert(x);
    } else if(array[0]=='p'){
      Iorder(root);
      printf("\n");
      Porder(root);
      printf("\n");
    } else if(array[0]=='d'){
      scanf("%d",&x);
      TreeDelete(TreeSearch(root,x));
    }
  }
  return 0;
}