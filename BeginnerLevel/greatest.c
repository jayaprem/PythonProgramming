#include <stdio.h>
int main(void) {
int a,b,c;
scanf("%d%d%d",&a,&b,&c);
if(((a>=0)||(a<=9))&&((b>=0)||(b<=9))&&((c>=0)||(c<=9)))
{
if(a>b&&a>c)
printf("a is greater");
else if(b>a&&b>c)
printf("b is greater");
else
printf("c is greater");
}
else
printf("enter a valid input");
return 0;
}
