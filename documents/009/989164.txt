#include <stdio.h>
#define N 25

typedef struct{
  int parent;
  int left;
  int right;
}Node;

Node node[N];

void preorder(int);
void inorder(int);
void postorder(int);

int main(){
  int i, j, n, id, child, sub;
  scanf("%d", &n);
  for(i = 0;i < n;i++){
    node[i].parent = node[i].left = node[i].right = -1;
  }
  for(i = 0;i < n;i++){
    scanf("%d", &id);
    for(j = 0;j < 2;j++){
      scanf("%d", &child);
      if(child != -1){
        node[child].parent = id;
        if(j == 0){
          node[id].left = child;
        }
        else{
          node[id].right = child;
        }
      }
    }
  }
  for(i = 0;i < n;i++){
    if(node[i].parent == -1){
      sub = i;
      break;
    }
  }
  printf("Preorder\n");
  preorder(sub);
  printf("\nInorder\n");
  inorder(sub);
  printf("\nPostorder\n");
  postorder(sub);
  printf("\n");
  return 0;
}
void preorder(int root){
  int i, j;
  printf(" %d", root);
  if(node[root].left != -1){
    i = node[root].left;
    preorder(i);
    if(node[root].right != -1){
      j = node[root].right;
      preorder(j);
    }
  }
  else{
    if(node[root].right != -1){
      j = node[root].right;
      preorder(j);
    }
  }
}

void inorder(int root){
  int i, j;
  if(node[root].left != -1){
    i = node[root].left;
    inorder(i);
    printf(" %d", root);
    if(node[root].right != -1){
      j = node[root].right;
      inorder(j);
    }
  }
  else{
    if(node[root].right != -1){
      printf(" %d", root);
      j = node[root].right;
      inorder(j);
    }
    else{
      printf(" %d", root);
    }
  }
}

void postorder(int root){
  int i, j;
  if(node[root].left != -1){
    i = node[root].left;
    postorder(i);
    if(node[root].right != -1){
      j = node[root].right;
      postorder(j);
    }
    printf(" %d", root);
  }
  else{
    if(node[root].right != -1){
      j = node[root].right;
      postorder(j);
      printf(" %d", root);
    }
    else{
      printf(" %d", root);
    }
  }
}