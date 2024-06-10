int main()
{
	int A[100],i,N;
	scanf("%d",&N);
	for(i=0;i<N;i++)
		scanf("%d",&A[i]);
	for(i=N;--i>=0;)
		printf("%d%s",A[i],i==0?"\n":" ");
	return 0;
}