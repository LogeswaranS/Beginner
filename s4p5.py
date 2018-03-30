#include <stdio.h>

int main(void) {
char ch[30],z,count=0;
printf("enter the string:\n");
scanf("%[^\n]s",ch);
while(ch[z]!='\0')
{
	
	if(ch[z]>='0'&&ch[z]<='9')
	{
	count++;
}
z++;
}
printf("%d",count);
	return 0;
}
