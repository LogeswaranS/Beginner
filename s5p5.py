#include<stdio.h>
void main()
{
	int a,i,count=0;
	printf("enter the numers:\n");
	scanf("%d",&a);
	while(a!=0)
	{
		a=a/10;
		count++;
	}
	printf("sum is %d",count);
}
