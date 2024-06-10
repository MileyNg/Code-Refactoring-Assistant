#include <stdio.h>
typedef struct {/*parent,left child ,right sibling*/
int p,l,r;
} node;
node T[27];
void Preorder(int );
void Inorder(int );
void Postorder(int );
int main()
{
int n,i,id,l,r;
scanf("%d",&n);
 
for(i=0;i<n;i++)
{
T[i].p = T[i].l = T[i].r = -1;
}
 
for(i=0;i<n;i++)
{
scanf("%d%d%d",&id,&l,&r);
T[id].l = l;
T[id].r = r;
T[l].p = id;
T[r].p = id;
}
 
for(i=0;i<n;i++) if(T[i].p == -1) break;
printf("Preorder\n");
Preorder(i);
printf("\n");
printf("Inorder\n");
Inorder(i);
printf("\n");
printf("Postorder\n");
Postorder(i);
printf("\n");
return 0;
}

void Preorder(int id)
{
printf(" %d",id);
if(id != -1)
{
if(T[id].l != -1) Preorder(T[id].l);
if(T[id].r != -1) Preorder(T[id].r);
}
}

void Inorder(int id)
{
if(id != -1)
{
if(T[id].l != -1) Inorder(T[id].l);
printf(" %d",id);
if (T[id].r != -1) Inorder(T[id].r);
}
}
void Postorder(int id)
{
if(id != -1)
{
if(T[id].l != -1) Postorder(T[id].l);
if (T[id].r != -1) Postorder(T[id].r);
}
printf(" %d",id);
}