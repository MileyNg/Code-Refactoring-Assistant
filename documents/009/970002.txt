#include<stdio.h>
#include<string.h>
char S[100],St[100],T[100],c;
int P,Q,R,p,i,j,sp,St2[100],Res;
int not[3]={2,1,0};
int and[3][3]={{},{0,1,1},{0,1,2}};
int or[3][3]={{0,1,2},{1,1,2},{2,2,2}};
void pop(){T[p++]=St[--sp];}
void push(){St[sp++]=S[i];}
void NotPOP(){for(;St[sp-1]=='-';T[p++]=St[--sp]);}
int pop2(){return St2[--sp];}
void push2(int n){St2[sp++]=n;}


int cal()
{
	memset(St2,-1,sizeof(St2));
	for(i=sp=0;c=T[i];i++)
	{
		switch(T[i])
		{
		case '0':
		case '1':
		case '2':push2(T[i]-'0');break;
		case 'P':push2(P);break;
		case 'Q':push2(Q);break;
		case 'R':push2(R);break;
		case '*':push2(and[pop2()][pop2()]);break;
		case '+':push2(or[pop2()][pop2()]);break;
		case '-':push2(not[pop2()]);break;
		}
	}
	return St2[0];
}

int main()
{
	for(;scanf("%s",S),S[0]!='.';)
	{
		memset(St,0,sizeof(St));
		memset(T,0,sizeof(T));
		for(i=p=sp=0;S[i];i++)
		{
			switch(S[i])
			{
			case '0':
			case '1':
			case '2':
			case 'P':
			case 'Q':
			case 'R':T[p++]=S[i];NotPOP();break;
			case '(':push();break;
			case ')':pop();sp--;NotPOP();break;
			case '*':
			case '+':
			case '-':push();break;
			}
		}
		for(P=Res=0;P<3;P++)
			for(Q=0;Q<3;Q++)
				for(R=0;R<3;R++)
					if(cal()==2)
						Res++;
		printf("%d\n",Res);
	}
	return 0;
}