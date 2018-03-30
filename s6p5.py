#include<stdio.h>
int main()
{
int a,b,z;
printf("enter the numbers:\n");
scanf("%d %d",&a,&b);
z=(a*b);
printf("%d",z);
if(z%2==0)
{
printf("even %d");	
}
else
{
printf(" odd %d");
}
return 0;
}
