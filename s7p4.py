#include<stdio.h>
int main()
{
    int n,m,b,sum=0;
    scanf("%d%d",&n,&m);
    sum=n+m;
    b=sum%2;
    if(b==1)
    {
        printf("odd");
    }
    else
    {
        printf("even");
    }
    return 0;
}
