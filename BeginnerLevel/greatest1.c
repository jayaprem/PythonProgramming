#include<stdio.h>
#include<conio.h>
void main()
{
int a,b,c;
	scanf("%d%d%d",&a,&b,&c);
  if((isdigit(a))&&(isdigit(b))&&(isdigit(c)))
  {
		if(a>b&&a>c)
		printf("a is g.creater");
		else if(b>a&&b>c)
		printf("b is greater");
		else
		printf("c is greater");
   }
   else
   printf("enter a valid input");
 }
