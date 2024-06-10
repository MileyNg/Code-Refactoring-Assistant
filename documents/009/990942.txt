#include<stdio.h>
#include<stdlib.h>

struct node{
  struct node *right;
  struct node *left;
  struct node *parent;
  int key;
};
typedef struct node * Node;
#define NIL NULL

Node root;
int count =0;
int count2 = 0;
Node treeMinimum(Node x){
   while (x->left != NIL){
    x = x->left;
}
return x;
}



Node IterativetreeSearch(Node u, int k){
  while(u !=NIL && k !=u->key){
    if(k < u->key){
      u = u->left;

    }

    else u = u->right;
  }
  return u;

}


/*
Node treeSearch(Node u, int k){
  if(u == NIL || k == u->key) return u;

  if(k < u->key) 
  return treeSearch(u->left,k);
  
  else return treeSearch(u->right,k);
  
  }*/

Node treeSuccessor(Node x){
  Node y;
  if(x->right != NIL){
    return treeMinimum(x->right);
      }
  y = x->parent;

  while(y != NIL && x == y->right){
    x = y;
    y = y->parent;
  }
  return y;
}

void treeDelete(Node z){
  Node y; // node to be deleted
  Node x; // child of y
 
  if(z->left == NIL || z->right == NIL){
    y = z;
  }
  else {
    y = treeSuccessor(z);
  }

  if(y->left != NIL){
    x = y->left;
  } 
  else {
    x = y->right;
  }

  if(x != NIL){
    x->parent = y->parent;
  }
  if(y->parent == NIL){
    root = x;
  }
  else if(y == y-> parent ->left){
    y->parent->left =x;
  }
  else y-> parent -> right = x;

  
  if(y != z){
    z->key = y->key;
  } 

}

void insert(int k){
  Node y = NIL;
  Node x = root;
  Node z;

  z = malloc(sizeof(struct node));
  z->key = k;
  z->left = NIL;
  z->right = NIL;

  while(x != NIL){
    y = x;
    if(z->key < x->key){
      x = x->left;
    }
    else x = x->right; 
  }
  z->parent = y;

  if(y == NIL){
    root = z;
  }
  else if (z->key < y->key){
    y->left = z;
  }
  
  else y->right = z;
}

void inorder(Node u){
  if(u != NIL){
    inorder(u->left);
    printf(" ");
    printf("%d",u->key);
    inorder(u->right);
  }
 
}




void preorder(Node u){
  
  
    if (u != NIL) {
      printf(" ");
      printf("%d",u->key); 
      preorder(u->left);
      preorder(u->right);
    
 
    
    }
}

int main(){
  int n, i, x;
  //int ,num[500000];
  char com[20];
  scanf("%d", &n);
  //for ( i = 0; i < n; i++ ){num[i] = 0;}//???
  for ( i = 0; i < n; i++ ){
    scanf("%s", com);
    if ( com[0] == 'f' ){
      scanf("%d", &x);
      Node t = IterativetreeSearch(root, x);
      if ( t != NIL ){
	printf("yes\n"); 
	/*num[count] = 1;
	count++;
	*/
      }
      else {
	printf("no\n");
	/*num[count] = 2;
	  count++;*/
      }
    }
    else if ( com[0] == 'i' ){
      scanf("%d", &x);
      insert(x);
    } 
    

    else if ( com[0] == 'p' ){
      /*if(count2 == 0){
	for(j=0;j<n;j++){
	  if(num[j]==1)printf("yes\n");
	  else if(num[j]==2)printf("no\n");
	  else printf("");
	  count2 = 1;
	}
	}*/
	inorder(root);
	printf("\n");
	preorder(root);
	printf("\n");
	count = 0;
	
      }
    else if ( com[0] == 'd' ){
      scanf("%d", &x);
      treeDelete(IterativetreeSearch(root, x));
    }
  }

  return 0;
  }