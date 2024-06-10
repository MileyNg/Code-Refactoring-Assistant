#include<stdio.h>
#include<math.h>
#include<string.h>
int main(void)
{
  long int a,b;
  while(scanf("%ld %ld",&a,&b)!=EOF){
    long int max;
	max=(a>=b?a:b);
    long int i,j,count=0;
	long int s[31];
	int e=1;
	for(j=0;;j++){
	  if(e==0)
	    break;
	  e=0;
	  for(i=2;i<max/2;i++){
	    if(a%i==0 && b%i==0){
		  e=1;
		  a/=i;
		  b/=i;
		  s[j]=i;
		  count+=1;
		  break;
		}
      }
	}
	long int minkou=1,maxkou=1;
	for(i=0;i<count;i++)
	  minkou*=s[i];
	maxkou=minkou*a*b;
	printf("%ld %ld\n",minkou,maxkou);
  }
	

  return 0;
}