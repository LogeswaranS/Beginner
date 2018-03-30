#include<stdio.h>
void main()
{
	int z,a[20],max;
	for(z=1;z<=10;z++)
	{
		scanf("%d",&a[z]);
	}
		max=a[1];
		for(z=1;z<=10;z++)
		{
		if(a[z]>max)
		{
		max=a[z];	
		}
		}
	printf("greatest numeber is %d",max);
}
