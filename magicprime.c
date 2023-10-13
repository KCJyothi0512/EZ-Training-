#include<stdio.h>
int main()
{
	int n,rem,rev=0,i;
	scanf("%d",&n);
	for(i=2;i<=n/2;i++)
	{
		if(n%i==0)
		{
			printf("Not a prime");
		}
	}
	while(n!=0)
	{
		rem=n%10;
		rev=rev*10+rem;
		n=n/10;
	}
	printf("\nPrime no.");
	/*while(n!=0)
	{
		rem=n%10;
		rev=rev*10+rem;
		n=n/10;
	}
	/*for(i=2;i<n;i++)
	{
		if(n%i==0)
		{
			printf("Not a prime");
		}
	}
	printf("\nPrime no.");*/
}