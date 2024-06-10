#include <stdio.h>
typedef struct{
    int p, l, r;
} node;
node t[25];
void Preoder(int root){
    printf(" %d", root);
    if(t[root].l != -1) Preoder(t[root].l);
    if(t[root].r != -1) Preoder(t[root].r);
}
void Inorder(int root){
    if(t[root].l != -1) Inorder(t[root].l);
    printf(" %d", root);
    if(t[root].r != -1) Inorder(t[root].r);
}
void Postorder(int root){
    if(t[root].l != -1) Postorder(t[root].l);
    if(t[root].r != -1) Postorder(t[root].r);
    printf(" %d", root);}
int main(){
    int i, n, id;
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        t[i].p = -1;
        t[i].l = -1;
        t[i].r = -1;
    }
    for(i = 0; i < n; i++){
        scanf("%d", &id);
        scanf("%d%d", &t[id].l, &t[id].r);
        if(t[id].l != -1) t[t[id].l].p = id;
        if(t[id].r != -1) t[t[id].r].p = id;
    }
    printf("Preorder\n");
    for(i = 0; i < n; i++){
        if(t[i].p == -1){
            Preoder(i);
            printf("\nInorder\n");
            Inorder(i);
            printf("\nPostorder\n");
            Postorder(i);
            printf("\n");
        }
    }
    return 0;
}