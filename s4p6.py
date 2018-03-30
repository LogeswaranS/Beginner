#include <stdio.h>

int main()
{
char ch[30];
int z=0;
static int spl=0,num=0,alp=0,spc=0;
printf("enter the string:\n");
scanf("%[^\n]s",ch);
while(ch[z]!='\0')
{
if((ch[z]>='a'&&ch[z]<='z')||(ch[z]>='A'&&ch[z]<='Z'))
{
	alp++;
}
else if(ch[z]>='0'&&ch[z]<='9')
{
	num++;
}
else if(ch[z]==' ')
{
	spc++;
}
else
{
	spl++;	
}
z++;
}

printf("%d",spl);
	return 0;
}
