#include<stdio.h>
int main()
{
	int a;
	printf("enter the number:\n");
	scanf("%d",&a);
	if(a>='0'&&a<='9')
	{
		printf("yes its in the range");
	}
	else
	{
		printf("no");
	}
	return 0;
}
