#include<stdio.h>
int main()
{
    int n,m=0,j;
    scanf("%d",&n);
    for(j=1;j<n;j++)
    {
        if(n%j==0)
        {
            m=m+1;
        }
            }
    if(m==0)
    {
        printf("prime");
    }
    else
    {
        printf("not a prime");
    }
    return 0;
}
