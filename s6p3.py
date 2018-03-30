#include<stdio.h>
int main()
{
	int z,sum=0,rem=0;
	printf("enter the number");
	scanf("%d",&z);
while(z!=0)
{
	rem=z%10;
	sum=sum+rem;
	z=z/10;
}
	printf("%d",sum);
	return 0;
}
