#include <stdio.h>

typedef struct _tree_t {
	int p, l, r;
} tree_t;

void print_preorder(int depth, tree_t tree[], int id, int n) {
	printf(" %d", id);
	if(tree[id].l != -1) print_preorder(depth+1, tree, tree[id].l, n);
	if(tree[id].r != -1) print_preorder(depth+1, tree, tree[id].r, n);
}

void print_inorder(int depth, tree_t tree[], int id, int n) {
	if(tree[id].r == -1 && tree[id].l == -1) {
		printf(" %d", id);
	} else if(tree[id].r == -1) {
		print_inorder(depth+1, tree, tree[id].l, n);
		printf(" %d", id);
	} else if(tree[id].l == -1) {
		printf(" %d", id);
		print_inorder(depth+1, tree, tree[id].r, n);
	} else {
		print_inorder(depth+1, tree, tree[id].l, n);
		printf(" %d", id);
		print_inorder(depth+1, tree, tree[id].r, n);
	}
}

void print_postorder(int depth, tree_t tree[], int id, int n) {
	if(tree[id].r == -1 && tree[id].l == -1) {
		printf(" %d", id);
	} else if(tree[id].r == -1) {
		print_postorder(depth+1, tree, tree[id].l, n);
		printf(" %d", id);
	} else if(tree[id].l == -1) {
		print_postorder(depth+1, tree, tree[id].r, n);
		printf(" %d", id);
	} else {
		print_postorder(depth+1, tree, tree[id].l, n);
		print_postorder(depth+1, tree, tree[id].r, n);
		printf(" %d", id);
	}
}

int main(void) {
	tree_t tree[30];
	int i, n;
	int id, r, l, root;
	
	scanf("%d\n", &n);
	for(i=0;i<n;i++) {
		tree[i].p = -1;
		tree[i].r = -1;
		tree[i].l = -1;
	}
	
	for(i=0;i<n;i++) {
		scanf("%d %d %d\n", &id, &l, &r);
		tree[id].r = r;
		tree[id].l = l;
		if(r != -1) tree[r].p = id;
		if(l != -1) tree[l].p = id;
	}

	for(i=0;i<n;i++) {
		if(tree[i].p == -1) {
			root = i;
			break;
		}
	}

	printf("Preorder\n");
	print_preorder(0, tree, root, n);
	printf("\n");

	printf("Inorder\n");
	print_inorder(0, tree, root, n);
	printf("\n");

	printf("Postorder\n");
	print_postorder(0, tree, root, n);
	printf("\n");
	
	return 0;
}