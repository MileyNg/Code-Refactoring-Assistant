#include <stdio.h>

int main()
{
  int n[10000],q[500];
  int a,b,i,j,count=0;

  scanf("%d",&a);
  for(i=0;i<a;i++){
    scanf("%d",&n[i]);
  }
  scanf("%d",&b);
  for(j=0;j<b;j++){
    scanf("%d",&q[j]);
  }

  for(i=0;i<a;i++){
    for(j=0;j<b;j++){
      if(n[i]==q[j])
	count++;
    }
  }

  printf("%d\n",count);
return 0;
}