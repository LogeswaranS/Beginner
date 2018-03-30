#include<stdio.h>
    int main()
    {
        char ch[20];
        int j,count=0;
        scanf("%[^\n]s",&ch);
        while(ch[j]!='\0')
        //for(j=0;ch[j]!='\0';j++)
        {
            if(ch[j]==' ')
            {
                count++;
            }
            j++;
        }
        printf("%d",count+1);
     
        return 0;
    }
     
