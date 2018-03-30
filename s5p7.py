#include <stdio.h>

int main() 
{
int x,y,n,t=0,a[30];
printf("enter the number:\n");
scanf("%d",&n);
for(x=0;x<n;x++)
{
	scanf("%d",&a[x]);
}
for(x=0;x<n;x++)
{
	for(y=0;y<n;y++)
	{
		if(a[x]>a[y])
		{
			t=a[x];
			a[x]=a[y];
			a[y]=t;
		}
	}
	}
printf("%d ",a[0]);
printf("%d",a[n-1]);	
return 0;
}
