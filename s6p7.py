#include<stdio.h>
int main()
{
	int x,y;
	printf("enter the two numbers:\n");
	scanf("%d%d",&x,&y);
	x=x+y;
	y=x-y;
	x=x-y;
	printf("after swapping %d %d",x,y);
}
