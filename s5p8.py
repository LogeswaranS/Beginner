#include<stdio.h>
int main()
{
	int x,n,a[39],sum=0,avg=0;
	printf("enter the number");
	scanf("%d",&n);
	for(x=0;x<n;x++)
	{
		scanf("%d",&a[x]);
	}
	for(x=0;x<n;x++)
	{
		sum=sum+a[x];
		avg=sum/n;
	}
	printf("%d",avg);
}
