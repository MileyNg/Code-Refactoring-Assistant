#include <stdio.h>
#include <string.h>
typedef struct {
  char mark;
  int value;
}Card;

void swap(Card *in,Card *out)
{
  Card temp;
  int i,j;
  temp.mark = out->mark;
  temp.value = out->value;
  out->mark = in->mark;
  out->value = in->value;
  in->mark = temp.mark;
  in->value = temp.value;
}

void Print(Card *in,int num)
{
  int i;
  for(i=0;i<num;i++)
    {
      printf("%c%d",in[i].mark,in[i].value);
      if (i<num-1) printf(" ");
    }
  printf("\n");
}
int num_hantei(Card *kai,Card *moto,int num,int *kazu)
{
  int i,j;
  int flag =0;
  for (i=0;i<num;i++)
    {
      if(kai[i].value == kai[i+1].value) 
	{
	  *kazu = i;
	  return 1;
	}
    }
 return 0;
}

int mark_hantei(Card *kai,Card *moto,int num,int kazu)
{
  int i,flag=0;
  for (i=0;i<num;i++)
    {
      if (kai[kazu].value == moto[i].value)
	{
	  if (kai[kazu].mark==moto[i].mark ) 
	    {
	    return 0;
	    }
	  else return 1;
	}
    }
}

int main()
{
  int i,j;
  int num,mini,kazu=0;
  int stable=0;
  Card A[36],B[36],C[36];

  scanf("%d",&num);
  for (i=0;i<num;i++)
    {
      scanf(" %c%d",&A[i].mark,&A[i].value);
      B[i].mark = A[i].mark;
      B[i].value = A[i].value;
      C[i].mark = A[i].mark;
      C[i].value = A[i].value;
    }

  /*bubble sort*/
  for (i=0;i<num;i++)
    {
      for (j=num-1;j>i;j--)
	{
	  if ( A[j].value < A[j-1].value) swap(&A[j],&A[j-1]);
	}
    }
  Print(A,num);
  if (num_hantei(A,C,num,&kazu)==1) stable=mark_hantei(A,C,num,kazu);
  if(stable == 1) printf("Not stable\n");
  else printf("Stable\n");

  /*select sort*/
  for(i=0;i<num;i++)
    {
      mini=i;
      for(j=i;j<num;j++)
	{
	  if (B[j].value < B[mini].value ) mini=j;
	}
      swap(&B[i],&B[mini]);
    }
  kazu =0;
  Print(B,num);
  if (num_hantei(B,C,num,&kazu)==1) stable=mark_hantei(B,C,num,kazu); 
  if(stable == 1) printf("Not stable\n");
  else printf("Stable\n");
  return 0;
}