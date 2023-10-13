#include<stdio.h>
main()
{
	int a=15,count=0;
	while(a)
	{
		count++;
		a=a&(a-1);
	}
	printf("Count set bits=%d",count);
}