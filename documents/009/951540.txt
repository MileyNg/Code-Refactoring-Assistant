#include <stdio.h>
   struct yami
{
   double kinri;
   int fusai;

};
int main (void)
{
   int i,week;
   struct yami a;
   a.kinri=0.05;
   a.fusai=100000;
   scanf("%d",&week);
   for(i=0;i<week;i++)
   {
      a.fusai*=(1+a.kinri);
   }
      if(a.fusai%1000!=0)
   {
      a.fusai/=10000;
      a.fusai+=1;
      a.fusai*=10000;
   }
   printf("%d\n",a.fusai);
   return 0;
}