#include<stdio.h>
#include<stdlib.h>

typedef struct node{
  struct node *right;
  struct node *left;
  struct node *parent;
  int key;
}node;
typedef node* Node;
#define NIL NULL

Node root;

Node treeMinimum(Node x){
  while (x->left != NIL) x = x->left;
  return x;
}

Node treeSearch(Node u, int key){
  while (u != NIL && u->key != key) {
    if (key < u->key) u = u->left;
    else u = u->right;
  }
  return u;
}

Node treeSuccessor(Node x){
  Node y;

  if (x->right != NIL) return treeMinimum(x->right);

  y = x->parent;

  while (y != NIL && x == y->right) {
    x = y;
    y = y->parent;
  }

  return y;
}

void treeDelete(Node z){
  Node y; // node to be deleted
  Node x; // child of y

  if (z->left == NIL || z->right == NIL) y = z;
  else y = treeSuccessor(z);

  if (y->left != NIL) x = y->left;
  else x = y->right;

  if (x != NIL) x->parent = y->parent;

  if (y->parent == NIL) root = x;
  else if (y == y->parent->left) y->parent->left = x;
  else y->parent->right = x;

  if (y != z) z->key = y->key;

}

void insert(int key){
  Node y = NIL;
  Node x = root;
  Node z;

  z = (Node)malloc(sizeof(node));
  z->key = key;
  z->left = NIL;
  z->right = NIL;

  while (x != NIL) {
    y = x;
    if (z->key < x->key) x = x->left;
    else x = x->right;
  }

  z->parent = y;
  if (y == NIL) root = z;
  else if (z->key < y->key) y->left = z;
  else y->right = z;

}

void inorder(Node u){
  if (u == NIL) return;
  inorder(u->left);
  printf(" %d", u->key);
  inorder(u->right);
}

void preorder(Node u){
  if (u == NIL) return;
  printf(" %d", u->key);
  preorder(u->left);
  preorder(u->right);
}

int main(){
  int n, i, key;
  char com[20];
  scanf("%d", &n);

  for ( i = 0; i < n; i++ ){
    scanf("%s", com);
    if ( *com == 'f' ){
      scanf("%d", &key);
      Node t = treeSearch(root, key);
      if ( t != NIL ) puts("yes");
      else puts("no");
    } else if ( *com == 'i' ){
      scanf("%d", &key);
      insert(key);
    } else if ( *com == 'p' ){
      inorder(root);
      puts("");
      preorder(root);
      puts("");
    } else if ( *com == 'd' ){
      scanf("%d", &key);
      treeDelete(treeSearch(root, key));
    }
  }

  return 0;
}