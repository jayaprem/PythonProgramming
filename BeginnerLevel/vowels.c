#include <stdio.h>
int main(void) {
char x;
scanf("%c",&x);
if(x>='a' && x<='z' || x>='A' && x<='Z')
{
if(x=='a'||x=='e'||x=='i'||x=='o'||x=='u'||x=='A'||x=='E'||x=='I'||x=='O'||x=='U')
{
printf("it is a vowel");
}
else
{
printf("\n it is a consonant");
}
}
else
printf("enter a valid input");
return 0;
}
