#include<stdio.h>
int main()
{
    char ch[20];
    int j;
    scanf("%s",&ch);
    if((ch[j]>'0'||ch[j]<'9')&&(ch[j]>='a'||ch[j]>='z')&&(ch[j]>='A'||ch[j]>='Z'))
    {
        printf("yes");
    }
    else
    {
        printf("no");
    }
    return 0;
}
