#include <stdio.h>
#include<string.h>

int main() {
	int count=0,z,len,len1;
	char ch1[30],ch2[30];
	scanf("%s %s",&ch1,&ch2);
	//printf("%d %d",strlen(ch1),strlen(ch2));
	len=strlen(ch1);
	len1=strlen(ch2);
	for(z=0;z<len;z++)
	{
		if(ch1[z]==ch2[z])
		{
			count++;
		}
	}
	if(count==len)
	{
		printf("%s\n",ch1);
	}
	
	if(ch1>ch2)
	{
		printf("%s",ch1);
	}
	else
{
	printf("%s",ch2);
}
	

	return 0;
}
