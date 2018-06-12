f=0
n=int(input())
while(n!=0):
	r=n%10
	p=r*r
	f=f+p
	n=n/10
print f
