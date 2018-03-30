#include<stdio.h>
int main()
{
	int i,r,j,t=0,a[90];
	printf("enter the number:");
	scanf("%d",&r);
	for(i=0;i<r;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<r;i++)
	{
		for(j=0;j<r;j++)
		{
		if(a[i]<a[j])
		{
		t=a[i];
		a[i]=a[j];
		a[j]=t;
		}
		}
	}
	printf("%d",a[r-1]);
}
