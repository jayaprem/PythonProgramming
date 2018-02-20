#include <stdio.h>
int main(void) {
int n;
scanf("%d",&n);
if(n!=0)
{
if(n%2==0)
printf("The given number is even");
else
printf("The given number is odd");
}
else
printf("enter a valid input");
return 0;
}
