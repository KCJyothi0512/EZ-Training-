#include<stdio.h>
int main()
{
	int n,a[10][10],i,j;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d\t",a[i][j]);
		}
		printf("\n");
	}
	for(i=0,j=0;i<n,j<n;i++,j++)
	{
		if(a[i][j]==0)
		{
			printf("count=1");
		}
		else
		{
			printf("count=0");
		}
	} /*
	for(i=0;i<n;i++)
	{
	    for(j=0;j<n;j++)
    	{
		if(i==j)
		{
			printf("count=1");
		}
		else
		{
			printf("count=0");
		}
	}
}
	/*for(i=0,j=0;j<n;i++)
	{
		if(a[i][j]==1)
		{
			printf("count=1");
		}
		else
		{
			printf("count=0");
		}
	}*/
}