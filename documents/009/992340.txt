#include<stdio.h>
#include<stdlib.h>

struct node{
        struct node *l;
        struct node *r;
        struct node *p;
        int key;
};

typedef struct node * Node;

void inorder(Node);
void preorder(Node);
void insert(int);
char* find(int);
void delete(int);
Node successor(Node);
Node minimum(Node);

Node root;

int main(void){
        int n,in;
        char input[7];
        int i;

        scanf("%d",&n);

        for(i=0;i<n;i++){
                scanf("%s",input);

                if(input[0]=='i'){
                        scanf("%d",&in);
                        insert(in);
                }
                else if(input[0]=='f'){
                        scanf("%d",&in);
                        printf("%s\n",find(in));
                }
                else if(input[0]=='d'){
                        scanf("%d",&in);
                        delete(in);
                }
                else{
                        if(root!=NULL){
                                inorder(root);
                                printf("\n");
                                preorder(root);
                                printf("\n");
                        }
                }
        }

        return 0;
}


void insert(int in){
        Node new,work,move;

        new=(Node)malloc(sizeof(struct node));
        new->key=in;
        new->l=NULL;
        new->r=NULL;

        work=NULL;
        move=root;
        while(move!=NULL){
                work=move;
                if(move->key > in){
                        move=move->l;
                }
                else{
                        move=move->r;
                }
        }

        new->p=work;
        if(work==NULL) root=new;
        else if(work->key > in) work->l=new;
        else work->r=new;

}


void inorder(Node work){
        if(work->l != NULL) inorder(work->l);
        printf(" %d",work->key);
        if(work->r != NULL) inorder(work->r);
}


void preorder(Node work){
        printf(" %d",work->key);
        if(work->l != NULL) preorder(work->l);
        if(work->r != NULL) preorder(work->r);
}


char* find(int in){
        Node work;

        work=root;
        while(work!=NULL){
                if(work->key == in) return "yes";

                else if(work->key > in) work=work->l;
                else work=work->r;
        }

        return "no";
}


void delete(int in){
        Node del,work,work2;

        del=root;

        //search delete node
        while(del!=NULL){
                if(del->key==in) break;
                else if(del->key > in){
                        del=del->l;
                }
                else{
                        del=del->r;
                }
        }

        //can't find delete node
        if(del==NULL) return;

        if(del->l==NULL || del->r==NULL) work=del;
        else work=successor(del);

        if(work->l != NULL) work2=work->l;
        else work2=work->r;

        if(work2 != NULL) work2->p=work->p;

        if(work->p == NULL) root=work2;
        else if(work == work->p->l) work->p->l=work2;
        else work->p->r=work2;

        if(work != del) del->key=work->key;

        free(work);
}


Node successor(Node work){
        Node work2;

        if(work->r != NULL) return minimum(work->r);

        work2=work->p;
        while(work2!=NULL && work==work2->r){
                work=work2;
                work2=work2->p;
        }

        return work2;
}


Node minimum(Node work){
        while(work->l != NULL) work=work->l;

        return work;
}