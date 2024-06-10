#include <stdio.h>
#include <math.h>
int sosuu(int );
int main(){
  int i,j,n,key,c=0;
  int *a;
  
  scanf("%d",&n);

a=malloc(n*sizeof(int));

  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }

  for(i=1;i<n;i++){
    key=a[i];
    j=i-1;
    while(j>=0 && a[j]>key){
      a[j+1]=a[j];
      j--;
    }
    a[j+1]=key;
  }
  c+=sosuu(a[0]);
  for(i=1;i<n;i++){
    if (a[i]!=a[i-1]){
     c += sosuu(a[i]); 
    }
  }
  printf("%d\n",c);
  free(a);
  return 0;
}

int sosuu(int x){
  int i,j=0;
  if(x==1)return 0;
  for(i=2; i <= sqrt(x) ;i++){
    if(x%i==0)return 0;
  }
  return 1;
}