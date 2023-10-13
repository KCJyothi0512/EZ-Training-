#include<stdio.h>
int main() //n=16,7,32,-100
{
	int count=0,n=32;
	while(n)
	{
		count++;
		n=n&(n-1);
	}
	if(count==1)
	{
		printf("true");
	}
	else
	{
		printf("false");
	}
}