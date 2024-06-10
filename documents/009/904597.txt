int main()
{
	int x,y;
	char c;
	for(;scanf("%d %c %d",&x,&c,&y),c!='?';)
	{
		switch(c)
		{
		case '+':printf("%d\n",x+y);break;
		case '-':printf("%d\n",x-y);break;
		case '*':printf("%d\n",x*y);break;
		case '/':printf("%d\n",x/y);break;
		}
	}
	return 0;
}