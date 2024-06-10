#include <stdio.h>

#define N 100001
#define NIL -1

#define INNER_NODE 1
#define LEAF -1
#define ROOT 0

typedef struct {
	int parent;
	int left;
	int right;
} Node;

Node node[N];

void initNode(int n) {
	int i;

	for (i = 0; i < n; i++) {
		node[i].parent = NIL;
		node[i].left = NIL;
		node[i].right = NIL;
	}
}

void createTree(int n) {
	int nodeId, i;

	initNode(n);

	for (i = 0; i < n; i++) {
		scanf("%d", &nodeId);
		scanf("%d %d", &node[nodeId].left, &node[nodeId].right);
		if (node[nodeId].left != NIL) {
			node[node[nodeId].left].parent = nodeId;
		}
		if (node[nodeId].right != NIL) {
			node[node[nodeId].right].parent = nodeId;
		}
	}
}

int judgeNode(Node node) {

	if (node.parent == NIL) {
		return ROOT;
	} else if (node.left == NIL && node.right == NIL) {
		return LEAF;
	} else {
		return INNER_NODE;
	}

	return 0;
}

void preorderTreeWalk(int id) {

	printf(" %d", id);
	if (node[id].left != NIL) {
		preorderTreeWalk(node[id].left);
	}
	if (node[id].right != NIL) {
		preorderTreeWalk(node[id].right);
	}

}

void inorderTreeWalk(int id) {

	if (node[id].left != NIL) {
		inorderTreeWalk(node[id].left);
	}
	printf(" %d", id);
	if (node[id].right != NIL) {
		inorderTreeWalk(node[id].right);
	}
}

void postorderTreeWalk(int id) {

	if (node[id].left != NIL) {
		postorderTreeWalk(node[id].left);
	}
	if (node[id].right != NIL) {
		postorderTreeWalk(node[id].right);
	}
	printf(" %d", id);
}

int main() {
	int i, n;

	scanf("%d", &n);

	initNode(n);
	createTree(n);

	for (i = 0; i < n; i++) {
		if (judgeNode(node[i]) == ROOT) {
			break;
		}
	}

	puts("Preorder");
	preorderTreeWalk(i);
	puts("");

	puts("Inorder");
	inorderTreeWalk(i);
	puts("");

	puts("Postorder");
	postorderTreeWalk(i);
	puts("");

	return 0;
}