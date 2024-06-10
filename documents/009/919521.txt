#include<stdio.h>
   int main(void){
      int N,a,b,c,ir,ks;
      scanf("%d",&N);
         for(ks=0;ks<N;ks++){
         scanf("%d%d%d",&a,&b,&c);
         if(a<b)
            ir=a,a=b,b=ir;
         if(a<c)
            ir=a,a=c,c=ir;
         if(a*a==b*b+c*c)
            printf("YES\n");
         else
            printf("NO\n");
         }
   return 0;
}