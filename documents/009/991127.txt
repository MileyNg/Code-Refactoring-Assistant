#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
  long key;
  struct node *left;
  struct node *right;
} Node;

Node *root;

void insert(long key) {
  Node *newNode, *current;

  newNode = (Node *)malloc(sizeof(Node));
  newNode->key = key;

  if (root == NULL) {
    root = newNode;
    return;
  }

  current = root;
  while (1) {
    if (newNode->key < current->key) {
      if (current->left == NULL) {
	current->left = newNode;
	break;
      } else {
	current = current->left;
      }
    } else {
      if (current->right == NULL) {
	current->right = newNode;
	break;
      } else {
	current = current->right;
      }
    }
  }
  current = newNode;

}

void inorderTreeWalk(Node* node) {
  if (node != NULL) {
    inorderTreeWalk(node->left);
    printf(" %ld", node->key);
    inorderTreeWalk(node->right);
  }
}

void preorderTreeWalk(Node* node) {
  if (node != NULL) {
    printf(" %ld", node->key);
    preorderTreeWalk(node->left);
    preorderTreeWalk(node->right);
  }
}

int main(void) {
  int n, i;
  long arg;
  char command[80];

  scanf("%d", &n);

  for (i = 0; i < n; i++) {
    scanf("%s", command);
    if (strcmp(command, "insert") == 0) {
      scanf("%ld", &arg);
      insert(arg);
    } else {
      inorderTreeWalk(root);
      printf("\n");
      preorderTreeWalk(root);
      printf("\n");
    }
  }


  return 0;
}