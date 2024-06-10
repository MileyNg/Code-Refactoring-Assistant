#include<stdio.h>
#define MAX 100005
#define NIL -1
 
/*
 p: parent
 l: left-child
 r: right sibling
 */
 
struct Node{
    int p, l, r;
};
struct Node T[MAX]; // Tree
int n;

void Preorder(int u){
  if(u != NIL){
  printf(" %d",u);  
  Preorder(T[u].l); 
  Preorder(T[u].r);
  }
}

void  Inorder(int u){
  if(u != NIL){
   Inorder(T[u].l); 
  printf(" %d",u);
 Inorder(T[u].r);
  }
}

void  Postorder(int u){
 if(u != NIL){
Postorder(T[u].l); 
Postorder(T[u].r); 
 printf(" %d",u);
}

}

main(){
  int i, j, d, v, c, l;
     
    scanf("%d", &n);
     
    for ( i = 0; i < n; i++ ) {
        T[i].p = T[i].l = T[i].r = NIL;
    }
    for (i = 0; i <n ; i++){
      scanf("%d %d %d", &v, &d, &c);
             T[d].p=v;
	     T[c].p=v;
             T[v].l=d;
             T[v].r=c;
 
    }
     
    /*...*/
    printf("Preorder\n");
    Preorder(0);
    printf("\n");
    printf("Inorder\n");
    Inorder(0);
    printf("\n");
    printf("Postorder\n");
    Postorder(0);
    printf("\n");
    return 0;
}