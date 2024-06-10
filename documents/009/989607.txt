#include <stdio.h>
 
#define MAX 100000
#define nil -1
 
struct Node{
  int y; 
  int l; 
  int r; 
};
 
void preorder(int u);
void inorder(int u);
void postorder(int u);
 
struct Node T[MAX];
int n;
 
main(){
  int i,j,v,c,root;
 
  scanf("%d",&n); 
 
  for(i=0;i<n;i++){
    T[i].y=nil;
    T[i].l=nil;
    T[i].r=nil;
  }
 
  for(i=0;i<n;i++){
    scanf("%d",&v); 
 
    for(j=0;j<2;j++){
      scanf("%d",&c); 
 
      if(j==0){
    T[v].l=c;  
      } else {
    T[v].r=c;
      }
    T[c].y=v;       
    }
  }
 
  for(i=0;i<n;i++){
    if(T[i].y==nil){
      root=i;
      break;
    }
  }
 
  printf("Preorder\n");
  preorder(root);
  printf("\n");
  printf("Inorder\n");
  inorder(root);
  printf("\n");
  printf("Postorder\n");
  postorder(root);
  printf("\n");
  
  return 0;
}
 
 
void preorder(int u){
 
  printf(" %d",u);
  if(T[u].l!=nil) preorder(T[u].l);
  if(T[u].r!=nil) preorder(T[u].r);
 
}
 
void inorder(int u){
 
  if(T[u].l!=nil) inorder(T[u].l);
  printf(" %d",u);
  if(T[u].r!=nil) inorder(T[u].r);
}
 
void postorder(int u){ 
  
  if(T[u].l!=nil) postorder(T[u].l);
  if(T[u].r!=nil) postorder(T[u].r);
  printf(" %d",u);
 
}