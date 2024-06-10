#include<stdio.h>
#include<stdlib.h>

#define NIL NULL

struct node{
  struct node *l;
  struct node *r;
  struct node *p;
  int key;
};

typedef struct node * Node;

Node root;

void Preorder(Node t){
  printf(" %d",t->key);
  if(t!=NIL){
    if(t->l!=NIL)Preorder(t->l);
    if(t->r!=NIL)Preorder(t->r);
  }
}

void Inorder(Node t){
  
  if(t!=NIL){
    if(t->l!=NIL){
      Inorder(t->l);
      }
    printf(" %d",t->key);
    
    if(t->r!=NIL){
      Inorder(t->r);
      }
  }
}

void insert(int k){
  Node y=NIL;
  Node x=root;
  Node z;

  z = malloc(sizeof(struct node));
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

Node Search(Node t,int k){
  if(t==NIL || k==t->key) return t;
  if(k<t->key) return Search(t->l,k);
  else return Search(t->r,k);
}

Node Minimum(Node t){
  while(t->l!=NIL){
    t=t->l;
  }
  return t;
}

Node Successor(Node t){
  if(t->r!=NIL)return Minimum(t->r);
  Node y=t->p;
  while(y!=NIL && t==y->r){
    t=y;
    y=y->p;
  }
  return y;
}

void Delete(Node z){
  Node y;
  Node x;

  if(z->l==NIL || z->r==NIL) y=z;
  else y=Successor(z);

  if(y->l!=NIL) x=y->l;
  else x=y->r;

  if(x!=NIL) x->p=y->p;
  else if(y==y->p->l) y->p->l=x;
  else  y->p->r=x;

  if(y!=z){
    z->key=y->key;
    z->l=y->l;
    z->r=y->r;
  }
  //return y;
}


main(){
  int n, i, x;
  char str[20];
  
  scanf("%d",&n);

  for ( i = 0; i < n; i++ ){
    scanf("%s",str);

    if(str[0]=='i'){
      scanf("%d",&x);
      insert(x);
    } 
    else if(str[0]=='p'){
      Inorder(root);
      printf("\n");
      
      Preorder(root);
      printf("\n");
    }
    else if(str[0]=='f'){
      scanf("%d",&x);
      Node s=Search(root,x);
      if (s!= NIL ) printf("yes\n");
      else printf("no\n");
    }
    else if(str[0]=='d'){
      scanf("%d",&x);
      Delete(Search(root, x));
    }
  }
  return 0;
}