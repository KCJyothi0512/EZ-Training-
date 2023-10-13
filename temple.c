#include<stdio.h>
int main()
{
	int a,b,c;
	scanf("%d",&a);
	b=21;
	c=a-b;
	(a<=b)? printf("buy lemons=%d",b-a): printf("valid no of lemons") :(a>b)? printf("extra lemons: ",c);
}