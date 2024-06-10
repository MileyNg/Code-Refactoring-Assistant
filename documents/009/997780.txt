#include<stdio.h>
#include<stdlib.h>
  
#define NIL NULL
  
struct node{
  struct node *r;
  struct node *l;
  struct node *parent;
  int key;
};
  
typedef struct node * Node;
  
Node root;
 
void pre(Node);
void ino(Node);
void ins(int);
void tD(Node);
Node tSuc(Node);
Node tM(Node);
Node tS(Node,int);
 
int main(){
  int n, i, x;
  char c[20];
  
  scanf("%d", &n);
  
  for ( i = 0; i < n; i++ ){
    scanf("%s", c);
    if ( c[0] == 'f' ){
      scanf(" %d", &x);
        
      Node t = tS(root, x);
        
      if ( t != NIL ) printf("yes\n");
      else printf("no\n");
    }
    else if ( c[0] == 'i' ){
      scanf("%d", &x);
      ins(x);
    }
    else if(c[0] == 'p' ){
      ino(root);
      printf("\n");
      pre(root);
      printf("\n");
    }
    else if(c[0] == 'd'){
      scanf("%d", &x);
      tD(tS(root, x));
    }
  }
    
  return 0;
}
 
 
Node tM(Node x){
  while(x->l != NIL){
    x = x->l;
  }
  return x;
}
  
Node tS(Node u, int k){
  while(u != NIL && k != u->key){
    if(k < u->key) u = u->l;
    else u = u->r;
  }
  return u;
}
  
Node tSuc(Node x){
  Node y;
  
  if(x->r != NIL) return tM(x->r);
    
  y = x->parent;
    
  while(y != NIL && x == y->r){
    x = y;
    y = y->parent;
  }
  return y;
}
  
void tD(Node z){
  Node y;
  Node x;
    
  if(z->l == NIL || z->r == NIL) y = z;
  else y = tSuc(z);
    
  if(y->l != NIL) x = y->l;
  else x = y->r;
    
  if(x != NIL) x->parent = y->parent;
    
  if(y->parent == NIL) root = x;
  else if(y == y->parent->l) y->parent->l = x;
  else y->parent->r = x;
    
  if(y != z){
    z->key = y->key;
      
  } 
}
  
void ins(int k){
  Node y = NIL;
  Node x = root;
  Node z;
    
  z = malloc(sizeof(struct node));
  z->key = k;
  z->l = NIL;
  z->r = NIL;
  
  while(x != NIL){
    y = x;
  
    if(z->key < x->key) x = x->l;
    else x = x->r;
  }
  z->parent = y;
    
  if(y == NIL) root = z;
  else if(z->key < y->key) y->l = z;
  else y->r = z; 
}
  
void ino(Node k){
  if(k != NIL){
    ino(k->l);
    printf(" %d", k->key);
    ino(k->r);
  }
}
  
void pre(Node k){
  if(k != NIL){
    printf(" %d", k->key);
    pre(k->l);
    pre(k->r);
  }
}