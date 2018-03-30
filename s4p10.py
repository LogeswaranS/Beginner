#include<stdio.h>
void main()
{
int z,n,t1=1,t2=1,t3;
scanf("%d",&n);
for(z=1;z<=n;z++)
{
printf("%d",t1);
t3=t1+t2;
t1=t2;
t2=t3;
}
}
