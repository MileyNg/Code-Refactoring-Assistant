#define _CRT_SECURE_NO_WARNINGS
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

Node treeMinimum(Node x){


}

Node treeSearch(Node u, int k){


}

Node treeSuccessor(Node x){


}

void treeDelete(Node z){
	Node y; // node to be deleted
	Node x; // child of y



}

Node sss(int k, Node x){
	if (x == NIL){ return x; }
	if (k < x->key){
		if (x->left != NIL){
			return sss(k, x->left);
		}
		else{
			return x;
		}
	}
	else{
		if (x->right != NIL){
			return sss(k, x->right);
		}
		else{
			return x;
		}
	}
}

void insert(int k){
	Node y = sss(k,root);
	Node z;

	z = malloc(sizeof(struct node));
	z->key = k;
	z->left = NIL;
	z->right = NIL;
	z->parent = y;

	if (y == NIL){ root=z; }
	else if (y->key < k){
		y->right = z;
	}
	else{
		y->left = z;
	}
}

void inorder(Node u){
	if (u->left != NIL)
		inorder(u->left);
	printf(" %d", u->key);
	if (u->right != NIL)
		inorder(u->right);	
}
void preorder(Node u){
	printf(" %d", u->key);
	if (u->left != NIL)
		preorder(u->left);
	if (u->right != NIL)
		preorder(u->right);
}


int main(){
	int n, i, x;
	char com[20];
	scanf("%d", &n);

	for (i = 0; i < n; i++){
		scanf("%s", com);
		if (com[0] == 'f'){
			scanf("%d", &x);
			Node t = treeSearch(root, x);
			if (t != NIL) printf("yes\n");
			else printf("no\n");
		}
		else if (com[0] == 'i'){
			scanf("%d", &x);
			insert(x);
		}
		else if (com[0] == 'p'){
			inorder(root);
			printf("\n");
			preorder(root);
			printf("\n");
		}
		else if (com[0] == 'd'){
			scanf("%d", &x);
			treeDelete(treeSearch(root, x));
		}
	}

	return 0;
}