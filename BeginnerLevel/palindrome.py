n=int(raw_input())
t=n
sum=0
while(t>0):
	a=t%10;
	sum=sum*10+a;
	t=t/10;
	
if(n==sum):
	print "palindrome"
else:
	print "not a palindrome"
